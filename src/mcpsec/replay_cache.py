import time

class ReplayCache:
    def __init__(self, ttl_seconds: int = 300):
        """
        Initializes a simple in-memory cache for nonces.

        Args:
            ttl_seconds: Time to live for each nonce (default 300 seconds = 5 minutes)
        """
        self.nonce_store = {}
        self.ttl_seconds = ttl_seconds

    def add_nonce(self, nonce: str):
        """
        Adds a nonce to the cache with an expiry time.

        Args:
            nonce: The nonce string to add.
        """
        expiry_time = time.time() + self.ttl_seconds
        self.nonce_store[nonce] = expiry_time

    def has_nonce(self, nonce: str) -> bool:
        """
        Checks if the nonce has already been used.

        Args:
            nonce: The nonce string to check.

        Returns:
            True if nonce exists and is not expired, False otherwise.
        """
        self._cleanup()
        expiry = self.nonce_store.get(nonce)
        if expiry and expiry > time.time():
            return True
        return False

    def _cleanup(self):
        """
        Removes expired nonces from the store.
        """
        now = time.time()
        expired = [nonce for nonce, expiry in self.nonce_store.items() if expiry <= now]
        for nonce in expired:
            del self.nonce_store[nonce]
