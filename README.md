# Crypto Snapshot

Small command-line tool that fetches a 24h rolling ticker snapshot for a given trading pair using [ccxt](https://github.com/ccxt/ccxt).

It supports:
- Multiple exchanges (default: Binance)
- Human-readable or JSON output
- Listing symbols with optional prefix filter and limit

This is primarily a learning / portfolio project to show API integration and CLI tooling in Python.

---

## Requirements

- Python 3.10+ (tested on 3.x)
- `ccxt` (installed via `requirements.txt`)

Install dependencies:

```bash
pip install -r requirements.txt
