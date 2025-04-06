import time
from mcpsec.replay_cache import ReplayCache

def test_replay_cache_add_and_check():
    cache = ReplayCache(ttl_seconds=2)
    nonce = "testnonce"

    assert cache.has_nonce(nonce) == False
    cache.add_nonce(nonce)
    assert cache.has_nonce(nonce) == True

def test_replay_cache_expiry():
    cache = ReplayCache(ttl_seconds=1)
    nonce = "expirynonce"

    cache.add_nonce(nonce)
    assert cache.has_nonce(nonce) == True

    time.sleep(1.5)
    assert cache.has_nonce(nonce) == False