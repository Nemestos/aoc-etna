from day_abstract import Day
from day_helper import flatten
from time_helper import timeit


class Day04(Day):
    def __init__(self, input_file):
        super().__init__(input_file);

    def line_check(self, line):
        return all(i == "x" for i in line)

    def check_victory(self, grids):
        for g in grids:
            h = False
            v = False
            for i in g:
                h = max(h, self.line_check(i))
            for i in list(zip(*g)):
                v = max(v, self.line_check(i))
            if h or v:
                return True, g

        return False, []

    def apply_value(self, grid, value):
        for i in range(5):
            for j in range(5):
                x = grid[i][j]
                grid[i][j] = "x" if x == value else x

    def calculate_score(self, grid, last):
        flat = flatten(grid)
        return sum([i for i in flat if i!="x"])*last

    @timeit
    def part1(self) -> tuple[int, int]:
        input = self.input_list(int, '\n', True, ",")
        values = input[0]
        grids = input[1:]
        win = self.check_victory(grids)
        i = 0
        while not win[0] and i < len(values):
            for g in grids:
                self.apply_value(g, values[i])

            i += 1
            win = self.check_victory(grids)

        return self.calculate_score(win[1], values[i-1])

    @timeit
    def part2(self) -> int:
        input = self.input_list(lambda x: list(x.rstrip()))
