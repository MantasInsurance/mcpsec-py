import json
import base64
from nacl.signing import VerifyKey
from nacl.exceptions import BadSignatureError

class InvalidSignatureError(Exception):
    """Raised when a context signature fails verification."""
    pass

def verify_context(context: dict, public_key_bytes: bytes) -> bool:
    """
    Verifies a signed context dictionary.

    Args:
        context: The signed context dictionary (must include 'signature' field).
        public_key_bytes: The public key bytes to verify against.

    Returns:
        True if verification succeeds.

    Raises:
        InvalidSignatureError: If the signature is invalid.
    """
    if "signature" not in context:
        raise InvalidSignatureError("No signature found in context.")

    # Extract and remove signature
    signature_b64 = context["signature"]
    context_to_verify = dict(context)
    del context_to_verify["signature"]

    # Canonicalize JSON (must match signing format)
    canonical_json = json.dumps(context_to_verify, separators=(",", ":"), sort_keys=True)

    # Prepare for verification
    verify_key = VerifyKey(public_key_bytes)

    try:
        verify_key.verify(
            canonical_json.encode('utf-8'),
            base64.b64decode(signature_b64)
        )
    except BadSignatureError:
        raise InvalidSignatureError("Context signature verification failed.")

    return True
