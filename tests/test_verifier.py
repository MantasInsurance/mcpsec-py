from mcpsec.signer import sign_context
from mcpsec.verifier import verify_context, InvalidSignatureError
from nacl.signing import SigningKey
import pytest

def test_verify_valid_context():
    signing_key = SigningKey.generate()
    verify_key = signing_key.verify_key

    context = {
        "context_id": "test-id",
        "issuer": "test-issuer",
        "issued_at": "2025-04-06T00:00:00Z",
        "nonce": "testnonce",
        "schema_version": "1.0",
        "payload": {"user": "tester"}
    }

    signed_context = sign_context(context, signing_key.encode())
    assert verify_context(signed_context, verify_key.encode()) == True

def test_verify_invalid_context():
    signing_key = SigningKey.generate()
    verify_key = signing_key.verify_key

    context = {
        "context_id": "test-id",
        "issuer": "test-issuer",
        "issued_at": "2025-04-06T00:00:00Z",
        "nonce": "testnonce",
        "schema_version": "1.0",
        "payload": {"user": "tester"}
    }

    signed_context = sign_context(context, signing_key.encode())
    signed_context["payload"]["user"] = "evil-user"  # Tamper with context

    with pytest.raises(InvalidSignatureError):
        verify_context(signed_context, verify_key.encode())