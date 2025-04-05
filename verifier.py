import json
import base64
from nacl.signing import VerifyKey
from .exceptions import InvalidSignatureError

def verify_context(context: dict, public_key_bytes: bytes) -> bool:
    context_copy = dict(context)
    signature_b64 = context_copy.pop('signature', None)
    if not signature_b64:
        raise InvalidSignatureError("No signature found in context.")
    
    canonical_json = json.dumps(context_copy, separators=(",", ":"), sort_keys=True)
    verify_key = VerifyKey(public_key_bytes)
    
    try:
        verify_key.verify(canonical_json.encode('utf-8'), base64.b64decode(signature_b64))
    except Exception:
        raise InvalidSignatureError("Signature verification failed.")
    
    return True
