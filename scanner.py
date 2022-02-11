import threading
import websocket
import constants
from utility import download_klines
from json import loads

ws_base_url = "wss://stream.binance.com:9443"

class Scanner(threading.Thread):

    def __init__(self, coin, minor_tf, major_tf, rr_ratio, tf_continuity, flows, setups, records):
        self.coin = coin
        self.minor_tf = minor_tf,
        self.major_tf = major_tf,
        self.rr_ratio = rr_ratio
        self.tf_continuity = tf_continuity
        self.flows = flows
        self.setups = setups
        self.records = records

        self.major_flow = None
        self.major_sentiment = constants.NEUTRAL

        self.minor_klines_s = download_klines(coin, minor_tf, constants.MAX_KLINES_MINOR)
        self.major_klines_s = download_klines(coin, major_tf, constants.MAX_KLINES_MAJOR)
        self.mapping = {
            minor_tf: self.minor_klines_s,
            major_tf: self.major_klines_s
        }

        symbol = coin + "usdt"
        minor_stream = symbol + "@kline_" + minor_tf
        major_stream = symbol + "@kline_" + major_tf
        url = f"{ws_base_url}/stream?streams={minor_stream}/{major_stream}"

        self.ws = websocket.WebSocketApp(
            url = url,
            on_message = self.on_message,
            on_error   = self.on_error,
            on_close   = self.on_close,
            on_open    = self.on_open        
        )
        super().__init__()

    def on_open(self, ws):
        open_str = f"Scanner established: \n"
        open_str += f"      Coin: {self.coin.upper()}\n"
        open_str += f"      Minor timeframe: {self.minor_tf[0]}\n"
        open_str += f"      Major timeframe: {self.major_tf[0]}\n" if self.tf_continuity else ""
        open_str += f"      Minimum setup R:R of: {self.rr_ratio}\n"
        open_str += f"      Trading with full timeframe continuity...\n" if self.tf_continuity else ""
        print(open_str)
        
    def on_error(self, ws, error):
        print(f"Error: {error}")
    
    def on_close(self, ws):
        print("Connection closed.")

    def on_message(self, ws, message):
        # Extract data from payload
        payload = loads(message)
        data = payload['data']['k']
        start_time, timeframe = data['t'], data['i']
        o, h, l, c = data['o'], data['h'], data['l'], data['c']

        # Update klines data
        klines_struct = self.mapping[timeframe]
        klines_struct.update_data(o, h, l, c, start_time)

        # Run scanner
        self.run_scanner()

    def run(self):
        self.ws.run_forever()
    
    def get_thread_info(self):
        thread_info = f"{self.coin.upper()}USDT --- {self.minor_tf[0]}"
        thread_info += f"& {self.major_tf[0]} timeframes" if self.tf_continuity else " timeframe"
        thread_info += f" --- Timeframe Continuity: "
        thread_info += f"Yes" if self.tf_continuity else "No"
        return(thread_info)

    def run_scanner(self):
        self.update_major_state()
        setup_s = self.find_setup()

        if setup_s is None:
            return
        
        timeframe_continuity = (setup_s.get_sentiment == self.major_sentiment)
        if self.tf_continuity and not timeframe_continuity:
            return
            
        rr_ratio = setup_s.get_setup_values(self.minor_klines_s)["rr_ratio"]
        if rr_ratio < self.rr_ratio:
            return

        alert_data = {
            "thread_info": self.get_thread_info(),
            "trade_info": self.get_trade_info(setup_s)
        }

        if alert_data not in self.records["alerts"]:
            self.records["alerts"].append(alert_data)

    def get_trade_info(self, setup_s):
        sv = setup_s.get_setup_values(self.minor_klines_s)
        trigger, target = sv["trigger"], sv["target"]
        stop, rr_ratio = sv["stop"], sv["rr_ratio"]
        trade_info = f"Possible {setup_s.get_sentiment_str()} {setup_s.get_desc()}:\n"
        trade_info += f"        Trigger: {trigger}\n"
        trade_info += f"        Target: {target}\n"
        trade_info += f"        Stop: {stop}\n"
        trade_info += "        Reward ratio: {:.2f}\n".format(round(rr_ratio, 2))

        # matching timeframe continuity already checked...
        if self.tf_continuity: 
            trade_info += f"        Timeframe continuity!\n"
            trade_info += f"                {self.major_flow}"
            
        return trade_info

    def update_major_state(self):
        relative_directions = self.major_klines_s.get_relative_directions()
        for flow in self.flows:
            flow_dirs = flow["flow"]
            if relative_directions[-1 * len(flow_dirs):] == flow_dirs:
                self.major_flow = flow["desc"]
                self.major_sentiment = flow["sentiment"]
                return

    def find_setup(self):
        for setup in self.setups:
            if setup.is_setup(self.minor_klines_s): return setup

