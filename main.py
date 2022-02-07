from fileinput import filename
import time
import constants
import os
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

    file_name = None
    if config["print_to_txt_file"]:
        file_name = input("Please enter file to print alerts to, e.g. alerts.txt: ")
        while os.path.isfile(file_name):
            resp = input("File already exists! Would you like to replace it? y/n: ")
            if resp == "y":
                file = open(file_name, "w")
                file.close()
                break
            if resp == "n": 
                file_name = input("Please enter another file name: ")
        print(f"Printing alerts to: {file_name}")

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
    
    time.sleep(5)

    alert_idx = 0
    while True:
        temp = alert_idx
        for idx in range(temp, len(records["alerts"])):
            alert = records["alerts"][idx]
            thread_info, trade_info = alert["thread_info"], alert["trade_info"]
            print(thread_info)
            print(trade_info)
            if file_name is not None:
                file = open(file_name, "a")
                print(thread_info, file = file)
                print(trade_info, file = file)
                file.close()
            alert_idx += 1
