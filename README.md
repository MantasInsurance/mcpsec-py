# MCP-Sec Python SDK (`mcpsec-py`)

Reference Python SDK for the **Model Context Protocol Security (MCP-Sec)** standard.

MCP-Sec protects AI models from attacks by securing the **dynamic context payloads** that influence model behavior at runtime.

This SDK enables:
- Secure signing of context payloads
- Cryptographic verification of incoming contexts
- Schema validation for trusted data structures
- Replay attack protection (nonce-based)
- Audit-friendly logging of context events

---

## 📦 Features

- Lightweight, easy to integrate
- Ed25519-based digital signatures (default)
- JSON Schema validation
- Nonce cache for replay protection
- Designed for real-world model inference systems
- Apache 2.0 Licensed

---

## 🚀 Installation

```bash
pip install mcpsec
