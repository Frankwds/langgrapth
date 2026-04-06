"""
State schema for the Startup Due Diligence workflow.
"""

from typing import TypedDict, List, Optional, Annotated
from operator import add


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
    research_outputs: Annotated[List[dict], add]

    # ANALYSIS
    analysis_outputs: Annotated[List[dict], add]

    # SYNTHESIS
    full_report: Optional[str]
    investment_decision: Optional[dict]

    # METADATA
    current_stage: str
    errors: Annotated[List[str], add]
    retry_count: int
