from mcpsec.schema import validate_schema, SchemaValidationError
import pytest

def test_validate_correct_payload():
    schema = {
        "type": "object",
        "properties": {
            "user_id": {"type": "string"},
            "location": {"type": "string"},
        },
        "required": ["user_id", "location"]
    }

    payload = {
        "user_id": "user123",
        "location": "Dubai"
    }

    assert validate_schema(payload, schema) == True

def test_validate_incorrect_payload():
    schema = {
        "type": "object",
        "properties": {
            "user_id": {"type": "string"},
            "location": {"type": "string"},
        },
        "required": ["user_id", "location"]
    }

    payload = {
        "user_id": "user123"
        # missing location
    }

    with pytest.raises(SchemaValidationError):
        validate_schema(payload, schema)