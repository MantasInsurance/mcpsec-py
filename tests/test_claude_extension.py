from mcpsec.extensions.claude_extension import get_claude_context_schema
from mcpsec.schema import validate_schema

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
        "temperature": 0.5,
        "top_p": 0.9,
        "stream": False,
        "system": "You are a helpful assistant."
    }
    schema = get_claude_context_schema()
    assert validate_schema(payload, schema) == True

def test_claude_invalid_payload():
    payload = {
        "model": "claude-3-opus-20240229",
        # Missing 'messages' field
    }
    schema = get_claude_context_schema()
    try:
        validate_schema(payload, schema)
        assert False, "SchemaValidationError was expected"
    except Exception:
        assert True
