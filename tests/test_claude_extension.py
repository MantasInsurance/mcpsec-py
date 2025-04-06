from mcpsec.extensions.claude_extension import get_claude_context_schema
from mcpsec.schema import validate_schema
import pytest

def test_claude_schema_structure():
    schema = get_claude_context_schema()
    assert isinstance(schema, dict)
    assert "properties" in schema
    assert "required" in schema

def test_claude_valid_payload():
    payload = {
        "model": "claude-3-opus-20240229",
        "messages": [
            {"role": "user", "content": "Hello, Claude!"}
        ],
        "max_tokens": 1024,
        "temperature": 0.5,
        "top_p": 0.9,
        "stream": False,
        "system": "You are a helpful assistant.",
        "metadata": {"session_id": "abc123"}
    }
    schema = get_claude_context_schema()
    assert validate_schema(payload, schema) == True

def test_claude_invalid_payload_missing_max_tokens():
    payload = {
        "model": "claude-3-opus-20240229",
        "messages": [
            {"role": "user", "content": "Hello, Claude!"}
        ]
        # missing max_tokens
    }
    schema = get_claude_context_schema()
    with pytest.raises(Exception):
        validate_schema(payload, schema)
