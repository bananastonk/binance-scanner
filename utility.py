from binance.client import Client as BinanceClient
from klines import Klines
from setup import Setup

start_strs = {
    "1m": "20 minutes ago",
    "5m": "3 hours ago",
    "15m": "9 hours ago",
    "30m": "18 hours ago",
    "1h": "12 hours ago",
    "2h": "1 day ago",
    "4h": "2 days ago",
    "6h": "3 days ago",
    "8h": "4 days ago",
    "12h": "6 days ago",
    "1d": "12 days ago",
    "3d": "30 days ago",
    "1w": "10 weeks ago", 
    "1M": "10 months ago"
}

# public data, no need for API keys
def download_klines(coin, timeframe, max_klines):
    binance_client = BinanceClient()
    ticker = coin.upper() + "USDT"
    historical_data = binance_client.get_historical_klines(
        symbol = ticker, 
        interval = timeframe, 
        start_str = start_strs[timeframe])
    klines_struct = Klines(historical_data, max_klines)
    return klines_struct
    
def get_setups(config):
    setups = []
    for pattern in config["setups_configuration"]:
        for setup_d in config["setups_configuration"][pattern]:
            setups.append(
                Setup(
                    setup_d["desc"],
                    setup_d["setup"],
                    setup_d["active_kline"],
                    setup_d["sentiment"],
                    setup_d["trigger"],
                    setup_d["target"],
                    setup_d["stop"]                )
            ) if (config["scan_for"][pattern] is True) else None
    return setups

def get_flows(config, sentiment):
    flows = []
    for pattern in config["setups_configuration"]:
        for setup in config["setups_configuration"][pattern]:
            flow = [agg_dir[1] for agg_dir in setup["setup"]]
            flow.append(setup["major_triggered"])
            flows.append(flow) if setup["sentiment"] is sentiment else None
    return flows

