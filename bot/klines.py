from kline import Kline

class Klines():
    def __init__(self, historical_data, max_klines):
        self.historical_data = historical_data
        self.max_klines = max_klines
        self.klines = []
        self.kline_ids = []

        size = len(historical_data)
        for idx in range(size - max_klines, size, 1):
            kline_data = historical_data[idx]
            start_time = kline_data[0]
            self.kline_ids.append(start_time)
            o, h, l, c = kline_data[1], kline_data[2], kline_data[3], kline_data[4]
            kline_struct = Kline(o, h, l, c, start_time, None)

            if idx == size - max_klines:
                self.klines.append(kline_struct)
                continue

            previous_kline = self.klines[-1]
            kline_struct.update_relative_direction(previous_kline)
            kline_struct.update_color()
            self.klines.append(kline_struct)

    def get_kline_ids(self):
        return self.kline_ids

    def get_klines(self):
        return self.klines

    def get_relative_directions(self):
        return [kline.get_relative_direction() for kline in self.klines]

    def get_agg_directions(self):
        return [kline.get_agg_direction() for kline in self.klines]
        
    def update_data(self, o, h, l, c, start_time):
        if start_time not in self.kline_ids:
            self.klines.pop(0)
            self.kline_ids.pop(0)
            previous_kline = self.klines[-1]
            new_kline = Kline(o, h, l, c, start_time, None)
            new_kline.update_relative_direction(previous_kline)
            new_kline.update_color()
            self.klines.append(new_kline)
            self.kline_ids.append(start_time)
        else:
            idx = self.kline_ids.index(start_time)
            previous_kline = self.klines[idx - 1]
            active_kline = self.klines[idx]
            active_kline.update_relative_direction(previous_kline)
            active_kline.update_hlc(h, l, c)
            active_kline.update_color()

