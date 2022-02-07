import time
import constants
from config import config
from scanner import Scanner
from utility import get_setups, get_flows

def get_scanners(config, setups, flows, records):
    scanner_threads = []
    for coin in config["coins"]:
        scanner_thread = Scanner(
            coin = coin,
            minor_tf = config["coins"][coin]["minor_timeframe"],
            major_tf = config["coins"][coin]["major_timeframe"],
            rr_ratio = config["coins"][coin]["minimum_reward_to_risk"],
            tf_continuity = config["coins"][coin]["timeframe_continuity"],
            flows = flows,
            setups = setups,
            records = records
        )
        scanner_threads.append(scanner_thread)
    return scanner_threads

if __name__ == "__main__":

    print(".....")
    print("Initiating program...")
    print(".....")
    
    setups = get_setups(config)
    flows = {
        constants.BULLISH: get_flows(config, constants.BULLISH),
        constants.BEARISH: get_flows(config, constants.BEARISH)
    }
    records = {
        "last_updated": time.time(),
        "alerts": []
    }
    scanner_threads = get_scanners(config, setups, flows, records)
    for scanner_thread in scanner_threads:
        scanner_thread.start()
    
    alert_idx = 0
    while True:
        temp = alert_idx
        for idx in range(temp, len(records["alerts"])):
            alert = records["alerts"][idx]
            thread_info, trade_info = alert["thread_info"], alert["trade_info"]
            print(thread_info)
            print(trade_info)
            alert_idx += 1
