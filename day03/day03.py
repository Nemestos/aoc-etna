from day_abstract import Day


class Day03(Day):
    def __init__(self, input_file):
        super().__init__(input_file);

    def part1(self) -> tuple[int, int]:
        input = self.input_list(lambda x: list(x.rstrip()))
        transposed = list(zip(*input))
        gamma = ""
        espsilon = ""
        for i in transposed:
            gamma += max(i, key=lambda a: i.count(a))
            espsilon += min(i, key=lambda a: i.count(a))
        return int(gamma, 2) * int(espsilon, 2)

    def part2(self) -> int:
        input = self.input_list(lambda x: list(x.rstrip()))
        oxy = self.get_factor("1", input[::], max)
        co = self.get_factor("0", input[::], min)
        return int(oxy, 2) * int(co, 2)

    def get_factor(self, equal, oxy_rest, func):
        i = 0
        l = len(oxy_rest[0])
        while len(oxy_rest) != 1 and i < l:
            filtered = [j[i] for j in oxy_rest]
            m = func(filtered, key=lambda a: filtered.count(a))
            if filtered.count("1") == filtered.count("0"):
                m = equal
            oxy_rest = [j for j in oxy_rest if j[i] == m]
            i += 1
        return "".join(oxy_rest[0])
