import json
import base64
from nacl.signing import SigningKey

def sign_context(context: dict, private_key_bytes: bytes) -> dict:
    """
    Signs a context dictionary and returns it with a 'signature' field attached.

    Args:
        context: The context dictionary to be signed.
        private_key_bytes: The private key bytes (Ed25519) to sign with.

    Returns:
        A new context dictionary with a 'signature' field added.
    """
    context_to_sign = dict(context)
    context_to_sign.pop('signature', None)
    canonical_json = json.dumps(context_to_sign, separators=(",", ":"), sort_keys=True)
    signing_key = SigningKey(private_key_bytes)
    signed = signing_key.sign(canonical_json.encode('utf-8'))
    signature_b64 = base64.b64encode(signed.signature).decode('utf-8')
    signed_context = dict(context)
    signed_context['signature'] = signature_b64
    return signed_context
