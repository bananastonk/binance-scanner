import constants

class Kline():
    def __init__(self, o, h, l, c, start_time, relative_direction):
        self.o = o
        self.h = h
        self.l = l
        self.c = c
        self.start_time = start_time
        self.relative_direction = relative_direction
        self.color = None

    def update_relative_direction(self, previous_kline):
        prev_h, prev_l = previous_kline.get_h(), previous_kline.get_l()
        ob = self.h > prev_h and self.l < prev_l
        ib = self.h <= prev_h and self.l >= prev_l
        up = self.h > prev_h and self.l >= prev_l
        down = self.h <= prev_h and self.l < prev_l
        relative_direction = "3" if ob else "1" if ib else "2u" if up else "2d" if down else None
        self.relative_direction = relative_direction

    def get_relative_direction(self):
        return self.relative_direction

    def get_o(self):
        return self.o

    def get_h(self):
        return self.h
    
    def get_l(self):
        return self.l

    def get_c(self):
        return self.c

    def get_value_from_str(self, str):
        str_to_value_mapping = {
            "o": self.o,
            "h": self.h,
            "l": self.l,
            "c": self.c
        }
        return float(str_to_value_mapping[str])

    def update_color(self):
        self.color = constants.GREEN if (self.c > self.o) else constants.RED if (self.o > self.c) else constants.NEITHER

    def update_hlc(self, h, l, c):
        self.h = h
        self.l = l
        self.c = c

    def get_agg_direction(self):
        return (self.relative_direction, self.color,)
