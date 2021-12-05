from day_abstract import Day
from day_helper import flatten
from time_helper import timeit


class Day04(Day):
    def __init__(self, input_file):
        super().__init__(input_file);

    def line_check(self, line):
        return all(i == "x" for i in line)

    def anyone_win(self, grids):
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

    def check_victory(self, grid):
        h = False
        v = False
        for i in grid:
            h = max(h, self.line_check(i))
        for i in list(zip(*grid)):
            v = max(v, self.line_check(i))
        return h or v

    def apply_value(self, grid, value):

        for i in range(5):
            for j in range(5):
                x = grid[i][j]
                grid[i][j] = "x" if x == value else x

    def calculate_score(self, grid, last):
        flat = flatten(grid)
        return sum([i for i in flat if i != "x"]) * last

    @timeit
    def part1(self) -> tuple[int, int]:
        input = self.input_list(int, '\n', True, ",")
        values = input[0]
        grids = input[1:]
        win = self.anyone_win(grids)
        i = 0
        while not win[0] and i < len(values):
            for g in grids:
                self.apply_value(g, values[i])

            i += 1
            win = self.anyone_win(grids)

        return self.calculate_score(win[1], values[i - 1])

    @timeit
    def part2(self) -> tuple[int, int]:
        input = self.input_list(int, '\n', True, ",")
        values = input[0]
        grids = input[1:]
        i = 0
        wins = []
        while len(grids) > 0:
            winnable = []
            for g in grids:
                self.apply_value(g, values[i])
                if self.check_victory(g):
                    wins.append(g)
                    winnable.append(g)
            for g in winnable:
                grids.remove(g)

            i += 1

        return self.calculate_score(wins[-1], values[i - 1])
