from abc import ABC, abstractmethod

from day_helper import apply_func, split_arr


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

    def input_list(self, func=None, line_sep="", first=False, first_sep=","):
        lines = self.get_input().readlines()
        if line_sep != "":
            lines = split_arr(lines, '\n')
            if first:
                lines[0] = apply_func(func, lines[0][0].split(first_sep))
            for i in range(first, len(lines)):
                for j in range(len(lines[i])):
                    lines[i][j] = apply_func(func, lines[i][j].rstrip().split())
        else:
            lines = apply_func(func, lines)
        return lines
