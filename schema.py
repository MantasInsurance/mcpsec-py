from jsonschema import validate, ValidationError
from .exceptions import SchemaValidationError

def validate_schema(payload: dict, schema: dict) -> bool:
    try:
        validate(instance=payload, schema=schema)
    except ValidationError as e:
        raise SchemaValidationError(f"Schema validation error: {e.message}")
    return True
