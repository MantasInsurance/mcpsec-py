# src/mcpsec/extensions/claude_extension.py

"""
Extension module for Anthropic Claude context validation.
Provides schema definition for validating Claude API context payloads.
"""

CLAUDE_CONTEXT_SCHEMA = {
    "type": "object",
    "properties": {
        "model": {"type": "string"},
        "messages": {
            "type": "array",
            "items": {
                "type": "object",
                "properties": {
                    "role": {"type": "string"},
                    "content": {"type": "string"}
                },
                "required": ["role", "content"]
            }
        },
        "max_tokens": {"type": "integer"},
        "temperature": {"type": "number"},
        "top_p": {"type": "number"},
        "stream": {"type": "boolean"},
        "system": {"type": "string"},
        "metadata": {"type": "object"}
    },
    "required": ["model", "messages", "max_tokens"]
}

def get_claude_context_schema() -> dict:
    """
    Returns the JSON Schema definition for a Claude context.

    Returns:
        dict: JSON Schema for Claude context payload.
    """
    return CLAUDE_CONTEXT_SCHEMA
