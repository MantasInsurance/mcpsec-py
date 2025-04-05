import time

class ReplayCache:
    def __init__(self, expiry_seconds=300):
        self.nonces = {}
        self.expiry = expiry_seconds

    def seen(self, nonce: str) -> bool:
        now = time.time()
        self.cleanup(now)
        if nonce in self.nonces:
            return True
        self.nonces[nonce] = now
        return False

    def cleanup(self, now=None):
        now = now or time.time()
        self.nonces = {nonce: ts for nonce, ts in self.nonces.items() if now - ts < self.expiry}
