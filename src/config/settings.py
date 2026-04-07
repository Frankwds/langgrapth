"""Configuration settings for the due diligence workflow."""

# Model name mappings - short names to full IDs
MODEL_MAPPING = {
    "haiku": "claude-haiku-4-5-20251001",
    "sonnet": "claude-sonnet-4-20250514",
    "opus": "claude-opus-4-5-20251101",
    # Also allow full names
    "claude-haiku-4-5-20251001": "claude-haiku-4-5-20251001",
    "claude-sonnet-4-20250514": "claude-sonnet-4-20250514",
    "claude-opus-4-5-20251101": "claude-opus-4-5-20251101",
}


def get_model_id(model_name: str) -> str:
    """Get the full model ID from a short name.
    
    Args:
        model_name: Short name like 'haiku', 'sonnet', 'opus' or full ID
    
    Returns:
        Full model ID string
    """
    return MODEL_MAPPING.get(model_name, model_name)