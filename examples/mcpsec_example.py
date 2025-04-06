# examples/mcpsec_example.py

from mcpsec.signer import sign_context
from mcpsec.verifier import verify_context
from mcpsec.schema import validate_schema
from mcpsec.replay_cache import ReplayCache
from mcpsec.extensions.claude_extension import get_claude_context_schema
from nacl.signing import SigningKey
from datetime import datetime, timedelta

def main():
    # 1. Setup signing keys and cache
    signing_key = SigningKey.generate()
    verify_key = signing_key.verify_key
    cache = ReplayCache()

    # 2. Create a fake Claude context payload
    payload = {
        "model": "claude-3-opus-20240229",
        "messages": [
            {"role": "user", "content": "Hello, Claude!"}
        ],
        "max_tokens": 1024,
        "temperature": 0.5,
        "top_p": 0.9,
        "stream": False,
        "system": "You are a helpful assistant.",
        "metadata": {"session_id": "abc123"}
    }

    # 3. Wrap it inside MCP-Sec standard context
    from datetime import datetime, timezone
    issued_at = datetime.now(timezone.utc)
    expires_at = issued_at + timedelta(minutes=5)

    context_wrapper = {
        "context_id": "uuid-1234",
        "issuer": "api.example.com",
        "issued_at": issued_at.isoformat() + "Z",
        "expires_at": expires_at.isoformat() + "Z",
        "nonce": "unique-nonce-001",
        "schema_version": "1.0",
        "payload": payload
    }

    try:
        # Step 4: Validate payload schema (Claude context)
        schema = get_claude_context_schema()
        validate_schema(context_wrapper["payload"], schema)

        # Step 5: Sign the full context
        signed_context = sign_context(context_wrapper, signing_key.encode())

        # Step 6: Verify the signed context
        verify_context(signed_context, verify_key.encode())

        # Step 7: Replay protection
        nonce = signed_context["nonce"]
        if cache.has_nonce(nonce):
            raise Exception("Replay detected ❌")
        else:
            cache.add_nonce(nonce)

        print("\n✅ ACCEPTED: Context is valid, signed, verified, and fresh.\n")

    except Exception as e:
        print(f"\n❌ REJECTED: {str(e)}\n")

if __name__ == "__main__":
    main()
