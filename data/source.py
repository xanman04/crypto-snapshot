import ccxt
from dataclasses import dataclass, asdict

@dataclass(frozen=True)
class Snapshot:
    symbol: str
    high_24h: float
    low_24h: float
    open: float
    last: float
    pct_change_24h: float
    timestamp: str
    source: str

def make_exchange(name: str):
    # Returns a CCXT exchange instance for a given exchange name
    name = name.lower()
    if not hasattr(ccxt, name):
        raise ValueError(f'Exchange "{name}" not found in ccxt.')
    exchange = getattr(ccxt, name)
    return exchange({"enableRateLimit" : True, "options" : {"defaultType" : "spot"}})

def get_snapshot(ex_name: str, symbol: str) -> Snapshot:
    # Returns an immutable dataclass snapshot of a given ticker
    exchange = make_exchange(ex_name)
    exchange.load_markets()
    t = exchange.fetch_ticker(symbol)
    return Snapshot(
        t['symbol'], 
        t.get('high'),
        t.get('low'),
        t.get('open'),
        t.get('last'), 
        t.get('percentage'), 
        t['datetime'], 
        exchange.id
        )
        
if __name__ == "__main__":
    s = get_snapshot("CrYPtOcOM", "ETH/USDT")
    for i,j in asdict(s).items():
        print(f"\n{i} : {j}")