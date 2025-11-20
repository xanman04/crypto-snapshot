import data.source as src
from dataclasses import asdict
import argparse, json

def main():
    parser = argparse.ArgumentParser(description="Fetch a 24h rolling ticker snapshot via CCXT")
    parser.add_argument('-x', '--exchange', default="binance", 
                        help="Exchange, e.g. binance/cryptocom/coinbase (See CCXT docs for available exchanges)")
    parser.add_argument('-j', '--json', action='store_true', 
                        help="Returns JSON instead of plain text")
    parser.add_argument('-f', '--filter', 
                        help="Prefix filter for --list, e.g. eth or BTC")
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument('-s', '--symbol', 
                        help="Trading pair, e.g. ETH/USDT")
    group.add_argument('-l', '--list', 
                        nargs='?', 
                        const=10, 
                        type=int, 
                        help="List tickers for the chosen exchange (optional limit N, default 10). Example: -l 25")
    
    args = parser.parse_args()

    if not args.list and args.filter:
        print("ERROR: --filter can only be used with --list")
        raise SystemExit(1)

    if args.list is not None:
        try:
            ex = src.make_exchange(args.exchange)
            try:
                ex.load_markets()
                syms = sorted(ex.symbols)
            except Exception as e:
                print(f"ERROR: Failed too load markets from {ex.id}: {e}")
                raise SystemExit(1)

            if args.filter:
                prefix = args.filter.upper()
                syms = [s for s in syms if s.startswith(prefix)]

            limit = args.list

            if limit <= 0:
                print("ERROR: limit must be a positive integer")
                raise SystemExit(1)
            
            trimmed = syms[:limit]

        except Exception as e:
            print(f"ERROR: {e}")
            raise SystemExit(1)
        
        if args.json:
            print(json.dumps(trimmed))
        else:
            for sym in trimmed:
                print(sym)
            if len(syms) > limit:
                print(f'... ({len(syms) - limit} more)')
        
        raise SystemExit(0)

    try: 
        s = src.get_snapshot(args.exchange, args.symbol.upper())
    except Exception as e:
        print(f"ERROR: {e}")
        raise SystemExit(1)

    if args.json:
        print(json.dumps(asdict(s)))
    else:
        for i,j in asdict(s).items():
            print(f'{i} : {j}')

if __name__ == '__main__':
    main()