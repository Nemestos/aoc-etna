from day_abstract import Day
from day_helper import flatten
from time_helper import timeit


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return f'{self.x},{self.y}'


class Day05(Day):
    def __init__(self, input_file):
        super().__init__(input_file);

    def calculate_size(self, pos):
        width = 0
        height = 0
        for i in pos:
            width = max(width, i[0].x, i[1].x)
            height = max(width, i[0].y, i[1].y)
        return width, height

    def inter_lines(self, grid):
        total = 0
        for i in grid:
            for j in i:
                total += j >= 2
        return total

    def line_cover(self, pos, diag=False):
        a, b = pos[0], pos[1]
        if a.x == b.x:
            return [Point(a.x, i) for i in range(min(a.y, b.y), max(a.y, b.y) + 1)]
        elif a.y == b.y:
            return [Point(i, a.y) for i in range(min(a.x, b.x), max(a.x, b.x) + 1)]
        elif diag:
            x = (-1 if a.x > b.x else 1)
            y = (-1 if a.y > b.y else 1)
            # cas diagonale
            return [Point(i, j) for i, j in zip(range(a.x, b.x + 1 * x, x), range(a.y, b.y + 1 * y, y))]
        else:
            return []

    @timeit
    def part1(self) -> tuple[int, int]:
        input = self.input_list(lambda a: [Point(*list(map(int, i.split(",")))) for i in a.split(" -> ")])
        width, height = self.calculate_size(input)
        grid = []
        for i in range(height + 1):
            grid.append([0] * (width + 1))
        for i in input:
            cover = self.line_cover(i)
            if cover != []:
                for p in cover:
                    grid[p.y][p.x] += 1

        return self.inter_lines(grid)

    @timeit
    def part2(self) -> tuple[int, int]:
        input = self.input_list(lambda a: [Point(*list(map(int, i.split(",")))) for i in a.split(" -> ")])
        width, height = self.calculate_size(input)
        grid = []
        for i in range(height + 1):
            grid.append([0] * (width + 1))
        for i in input:
            cover = self.line_cover(i, True)
            if cover != []:
                for p in cover:
                    grid[p.y][p.x] += 1
        return self.inter_lines(grid)
