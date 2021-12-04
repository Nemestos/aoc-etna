import importlib
import os
import re
from day_abstract import Day


class AOC:
    def gets_dirs(self):
        return sorted([f for f in os.listdir() if re.search(r'day\d', f)])

    def get_days_objs(self) -> [Day]:
        dirs = self.gets_dirs()
        objs = []
        for x in dirs:
            mod = importlib.import_module(x + "." + x)
            objs += [getattr(mod, x.capitalize())(x + "/input.txt")]
        return objs

    def show_days(self, n):
        dirs = self.gets_dirs()
        print(dirs)
        print("DAYS".center(n, "-"))
        for i in dirs:
            print(i.upper())

    def len_day(self):
        return len(self.gets_dirs())

    def input_day(self):
        day = ""
        l = self.len_day()
        while not day.isnumeric() or (day.isnumeric() and not 1 <= int(day) <= l):
            day = input(f'SELECT DAY(1-{l})')
        day = int(day) - 1
        obj = self.get_days_objs()[day]
        return obj
