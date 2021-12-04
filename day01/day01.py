from day_abstract import Day
from time_helper import timeit


class Day01(Day):
    def __init__(self, input_file):
        super().__init__(input_file);

    @timeit
    def part1(self) -> int:
        input = self.input_list(lambda x: int(x))
        step1 = 0
        l = len(input)
        for i in range(1, l):
            step1 += input[i] > input[i - 1]

        return step1

    @timeit
    def part2(self) -> int:
        input = self.input_list(lambda x: int(x))
        step2 = 0
        l = len(input)
        for i in range(1, l - 2):
            step2 += sum(input[i:i + 3]) > sum(input[i - 1:i + 2])
        return step2
