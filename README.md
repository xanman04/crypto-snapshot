# Crypto Snapshot

Small command-line tool that fetches a 24h rolling ticker snapshot for a given trading pair using [ccxt](https://github.com/ccxt/ccxt).

It supports:
- Multiple exchanges (default: Binance)
- Human-readable or JSON output
- Listing symbols with optional prefix filter and limit

This is primarily a learning / portfolio project to show API integration and CLI tooling in Python.

---

## Requirements

- Python 3.10+ (tested on 3.13.1)
- `ccxt` (installed via `requirements.txt`)

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## Usage

Run all commands from the project root.
### List symbols

List the default 10 symbols (Binance):

```bash
python main.py -l
```

List 5 symbols and filter by prefix (case-insensitive):

```bash
python main.py -l 5 -f eth
```

Example output:

```text
ETH/AEUR
ETH/ARS
ETH/AUD
ETH/BIDR
ETH/BKRW
... (45 more)
```

---

### Get a snapshot for a trading pair

Fetch a 24h snapshot for `ETH/USDT` on Binance:

```bash
python main.py -s ETH/USDT
```

Example output:

```text
symbol : ETH/USDT
high_24h : 3565.84
low_24h : 3203.8
open : 3442.74
last : 3204.52
pct_change_24h : -6.919
timestamp : 2025-11-13T18:37:47.010Z
source : binance
```

Same output in JSON format:

```bash
python main.py -s ETH/USDT --json
```

Example JSON:

```json
{
    "symbol": "ETH/USDT",
    "high_24h": 3565.84,
    "low_24h": 3201.51,
    "open": 3442.49,
    "last": 3201.69,
    "pct_change_24h": -6.995,
    "timestamp": "2025-11-13T18:39:08.013Z",
    "source": "binance"
}
```

---
### Use a different exchange

Specify an exchange supported by ccxt:

```bash
python main.py -x coinbase -s ETH/USDT --json
```

Or list symbols from that exchange:

```bash
python main.py -x coinbase -l 10
```

Example output:

```text
00/USD
00/USDC
0G/USDC:USDC
1000BONK/USDC:USDC
1000FLOKI/USDC:USDC
1000MOG/USDC:USDC
1000PEPE/USDC:USDC
1000SATS/USDC:USDC
1000SHIB/USDC:USDC
1000TOSHI/USDC:USDC
... (1068 more)
```

---

## Notes & Limitations

- Snapshot fields depend entirely on what each exchange provides.
- Missing fields appear as `null` in JSON output.
- Symbols are normalized to uppercase internally (`eth/usdt` → `ETH/USDT`).
- Only spot markets are queried (`defaultType=spot`).
- This tool is intended as a small portfolio project, not production software.

---

## Possible Future Improvements

These are optional ideas to extend the tool:

- Derive 24h statistics from OHLCV data when missing.
- Support watchlists or multiple-symbol snapshots.
- Package as an installable CLI.

---

## License

This project is available under the MIT License.
