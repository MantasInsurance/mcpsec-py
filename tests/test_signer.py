from mcpsec.signer import sign_context
from nacl.signing import SigningKey

def test_sign_context_adds_signature():
    signing_key = SigningKey.generate()
    context = {
        "context_id": "test-id",
        "issuer": "test-issuer",
        "issued_at": "2025-04-06T00:00:00Z",
        "nonce": "testnonce",
        "schema_version": "1.0",
        "payload": {"user": "tester"}
    }
    signed_context = sign_context(context, signing_key.encode())

    assert "signature" in signed_context
    assert isinstance(signed_context["signature"], str)
    assert len(signed_context["signature"]) > 0