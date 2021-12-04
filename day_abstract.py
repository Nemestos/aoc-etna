from abc import ABC, abstractmethod
from time_helper import *


class Day(ABC):
    @abstractmethod
    def __init__(self, input_file):
        self.input = input_file


    @abstractmethod
    def part1(self) -> int:
        return 0

    @abstractmethod
    def part2(self) -> int:
        return 0

    def get_input(self):
        return open(self.input, 'r')

    def input_list(self, func=None):
        lines = self.get_input().readlines()
        if func is not None:
            return list(map(func, lines))
        return lines
