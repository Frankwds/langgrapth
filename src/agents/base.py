"""
Base agent wrapper for Claude Agent SDK calls.

Standardizes how all agents call the SDK, handles error catching,
and ensures consistent output format.
"""

import asyncio
import time
import json
from typing import List, Optional, Any
from pydantic import BaseModel

from ..config.settings import get_model_id


class AgentResult(BaseModel):
    """Standardized result from any agent call."""
    success: bool
    output: Optional[Any] = None
    raw_output: Optional[str] = None
    error: Optional[str] = None
    agent_name: str
    execution_time_ms: int

async def run_agent(
    agent_name: str,
    prompt: str,
    tools: Optional[List[str]] = None,
    model: str = "sonnet",
    system_prompt: Optional[str] = None,
    timeout_seconds: int = 60
) -> AgentResult:
    """Execute a single agent using Claude Agent SDK."""
    start_time = time.time()
    model_id = get_model_id(model)

    try:
        from claude_agent_sdk import (
            query, ClaudeAgentOptions, AssistantMessage,
            ResultMessage, TextBlock,
        )

        options = ClaudeAgentOptions(
            model=model_id,
            allowed_tools=tools if tools else [],
            permission_mode="bypassPermissions",
            cwd="/tmp"
        )

        output_text = ""

        async def execute():
            nonlocal output_text
            async for message in query(prompt=prompt, options=options):
                if isinstance(message, AssistantMessage):
                    for block in message.content:
                        if isinstance(block, TextBlock):
                            output_text += block.text
                elif isinstance(message, ResultMessage):
                    if message.result and not output_text:
                        output_text = message.result

        await asyncio.wait_for(execute(), timeout=timeout_seconds)

        elapsed_ms = int((time.time() - start_time) * 1000)
        return AgentResult(
            success=True,
            output=None,
            raw_output=output_text,
            error=None,
            agent_name=agent_name,
            execution_time_ms=elapsed_ms
        )

    except asyncio.TimeoutError:
        elapsed_ms = int((time.time() - start_time) * 1000)
        return AgentResult(
            success=False,
            output=None,
            raw_output=None,
            error=f"Timeout after {timeout_seconds}s",
            agent_name=agent_name,
            execution_time_ms=elapsed_ms
        )

    except Exception as e:
        elapsed_ms = int((time.time() - start_time) * 1000)
        return AgentResult(
            success=False,
            output=None,
            raw_output=None,
            error=str(e),
            agent_name=agent_name,
            execution_time_ms=elapsed_ms
        )