import jsonschema
from jsonschema import ValidationError

class SchemaValidationError(Exception):
    """Raised when context payload fails schema validation."""
    pass

def validate_schema(payload: dict, schema: dict) -> bool:
    """
    Validates the payload dictionary against a JSON Schema.

    Args:
        payload: The context payload to validate.
        schema: The JSON schema to validate against.

    Returns:
        True if payload is valid.

    Raises:
        SchemaValidationError: If validation fails.
    """
    try:
        jsonschema.validate(instance=payload, schema=schema)
    except ValidationError as e:
        raise SchemaValidationError(f"Schema validation failed: {str(e)}")

    return True