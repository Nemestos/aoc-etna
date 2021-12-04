from day_abstract import Day
from time_helper import timeit


class Day02(Day):
    def __init__(self, input_file):
        super().__init__(input_file);

    @timeit
    def part1(self) -> tuple[int, int]:
        input = self.input_list(lambda x: x.split())
        dirs = {"forward": (1, 0), "down": (0, 1), "up": (0, -1)}

        horizontal = 0
        depth = 0
        for i in input:
            x, y = dirs[i[0]]
            val = int(i[1])
            horizontal += x * val
            depth += y * val
        return horizontal * depth

    @timeit
    def part2(self) -> int:
        input = self.input_list(lambda x: x.split())
        dirs = {"forward": (1, 0, 0), "down": (0, 1, 1), "up": (0, -1, -1)}

        horizontal = 0
        depth = 0
        aim = 0
        for i in input:
            x, y, a = dirs[i[0]]
            val = int(i[1])
            aim += a * val
            horizontal += x * val
            depth += (aim * val) * x

        return horizontal * depth
