"""
State schema for the Startup Due Diligence workflow.
"""

from typing import TypedDict, List, Optional


class DueDiligenceState(TypedDict):
    """
    Central state object that flows through the LangGraph workflow.
    All agents read from and write to this state.
    """

    # INPUT
    startup_name: str
    startup_description: str
    funding_stage: Optional[str]

    # RESEARCH
    research_outputs: List[dict]

    # ANALYSIS
    analysis_outputs: List[dict]

    # SYNTHESIS
    full_report: Optional[str]
    investment_decision: Optional[dict]

    # METADATA
    current_stage: str
    errors: List[str]
    retry_count: int
