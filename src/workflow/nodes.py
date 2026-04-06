from typing import Dict, Any

from ..state.schema import DueDiligenceState


async def init_node(state: DueDiligenceState) -> Dict[str, Any]:
    """Initialize the workflow."""
    print("Running: init_node")
    print(f"  Startup: {state.get('startup_name')}")
    return {"current_stage": "init_complete"}


async def research_node(state: DueDiligenceState) -> Dict[str, Any]:
    """Run all research agents in parallel to gather raw data."""
    print("Running: research_node")
    print("Would run 5 research agents here...")
    return {
        "research_outputs": [{"agent": "stub", "success": True}],
        "current_stage": "research_complete",
    }


async def validate_research_node(state: DueDiligenceState) -> Dict[str, Any]:
    """Validate that research outputs are complete and sufficient."""
    print("Running: validate_research_node")
    return {"current_stage": "research_validated"}


async def analysis_node(state: DueDiligenceState) -> Dict[str, Any]:
    """Run all analysis agents in parallel to interpret research data."""
    print("Running: analysis_node")
    print("Would run 4 analysis agents here...")
    return {
        "analysis_outputs": [{"agent": "stub", "success": True}],
        "current_stage": "analysis_complete",
    }


async def synthesis_node(state: DueDiligenceState) -> Dict[str, Any]:
    """Generate the final report and investment decision from analysis outputs."""
    print("Running: synthesis_node")
    return {
        "full_report": "Stub report",
        "investment_decision": {"recommendation": "hold"},
        "current_stage": "synthesis_complete",
    }


async def output_node(state: DueDiligenceState) -> Dict[str, Any]:
    """Finalize and present the workflow output."""
    print("Running: output_node")
    print("Workflow complete!")
    return {"current_stage": "complete"}
