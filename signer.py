import json
import base64
from nacl.signing import SigningKey

def sign_context(context: dict, private_key_bytes: bytes) -> dict:
    context_copy = dict(context)
    context_copy.pop('signature', None)
    canonical_json = json.dumps(context_copy, separators=(",", ":"), sort_keys=True)
    
    signing_key = SigningKey(private_key_bytes)
    signature = signing_key.sign(canonical_json.encode('utf-8')).signature
    context['signature'] = base64.b64encode(signature).decode('utf-8')
    return context
