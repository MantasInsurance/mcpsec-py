from mcpsec.signer import sign_context
from mcpsec.verifier import verify_context
from mcpsec.schema import validate_schema
from mcpsec.replay_cache import ReplayCache
from nacl.signing import SigningKey
import json
import datetime

# Load schema
with open("examples/schemas/user_context_schema.json") as f:
    user_schema = json.load(f)

# Setup replay cache
replay_cache = ReplayCache()

# Generate keys (for demo only — normally keys are persistent)
signing_key = SigningKey.generate()
verify_key = signing_key.verify_key

# Simulate context creation
def create_context():
    now = datetime.datetime.utcnow()
    context = {
        "context_id": "uuid-1234",
        "issuer": "api.example.com",
        "issued_at": now.strftime("%Y-%m-%dT%H:%M:%SZ"),
        "expires_at": (now + datetime.timedelta(minutes=5)).strftime("%Y-%m-%dT%H:%M:%SZ"),
        "nonce": "random_nonce_123",
        "schema_version": "1.0",
        "payload": {
            "user_id": "user_001",
            "location": "UAE",
            "device": "mobile"
        }
    }
    return context

# Create and sign context
context = create_context()
signed_context = sign_context(context, signing_key.encode())

# Simulate receiving and verifying
try:
    # Step 1: Verify Signature
    verify_context(signed_context, verify_key.encode())
    
    # Step 2: Validate Schema
    validate_schema(signed_context["payload"], user_schema)
    
    # Step 3: Check Replay Protection
    if replay_cache.seen(signed_context["nonce"]):
        raise Exception("Replay Attack Detected")

    print("[ACCEPTED] Context verified, valid, and fresh.")

except Exception as e:
    print(f"[REJECTED] Context failed checks: {str(e)}")
