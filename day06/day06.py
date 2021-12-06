import collections
from copy import copy

from day_abstract import Day
from day_helper import flatten
from time_helper import timeit
import threading


class Day06(Day):
    DEFAULT_FISH = 6
    DEFAULT_NEW = 8

    def __init__(self, input_file):
        super().__init__(input_file);

    def handle_fish(self, fish_ind, all_fish):
        if all_fish[fish_ind] > 0:
            all_fish[fish_ind] -= 1
            return 0
        else:
            all_fish.append(self.DEFAULT_NEW)
            all_fish[fish_ind] = self.DEFAULT_FISH
            return 1

    @timeit
    def part1(self) -> tuple[int, int]:
        input = self.input_list(lambda a: [int(i) for i in a.split(",")])[0]
        l = len(input)
        for _ in range(80):
            temp = copy(l)
            for i in range(l):
                new = self.handle_fish(i, input)
                temp += new
            l = temp

        return l

    @timeit
    def part2(self) -> tuple[int, int]:
        input = self.input_list(lambda a: collections.Counter([int(i) for i in a.split(",")]))[0]

        print(input)

        for _ in range(256):
            new = {k - 1: v for k, v in input.items() if k > 0}
            if new.get(self.DEFAULT_NEW) is None:
                new[self.DEFAULT_NEW] = 0

            new[self.DEFAULT_NEW] += input.get(0) or 0

            if new.get(self.DEFAULT_FISH) is None:
                new[self.DEFAULT_FISH] = 0

            new[self.DEFAULT_FISH] += input.get(0) or 0
            input = new

        return sum(input.values())

