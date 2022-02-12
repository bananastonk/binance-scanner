from klines import Klines
import constants

class Setup():
    def __init__(self, desc, setup, active_kline, sentiment, trigger, target, stop):
        self.desc = desc
        self.setup = setup
        self.active_kline = active_kline
        self.sentiment = sentiment
        self.trigger_i, self.trigger_p = trigger[0], trigger[1]
        self.target_i, self.target_p = target[0], target[1]
        self.stop_i, self.stop_p = stop[0], stop[1]

    def is_setup(self, klines_struct):
        agg_directions = klines_struct.get_agg_directions()
        klines_setup = agg_directions[-1 - len(self.setup):-1]
        active_kline = klines_struct.get_klines()[-1].get_relative_direction()
        return ((self.setup == klines_setup) and self.active_kline == active_kline)

    def get_desc(self):
        return self.desc
    
    def get_sentiment(self):
        return self.sentiment
    
    def get_sentiment_str(self):
        return "Bullish" if (self.sentiment == constants.BULLISH) else "Bearish"

    def get_setup_values(self, klines_struct):
        setup_klines = klines_struct.get_klines()[-1 - len(self.setup) : -1]
        trigger = setup_klines[self.trigger_i].get_value_from_str(self.trigger_p)
        target = setup_klines[self.target_i].get_value_from_str(self.target_p)
        stop = setup_klines[self.stop_i].get_value_from_str(self.stop_p)
        rr_ratio = (target - trigger) / (trigger - stop)
        setup_values = {
            "trigger": trigger,
            "target": target,
            "stop": stop,
            "rr_ratio": rr_ratio
        }
        return setup_values
