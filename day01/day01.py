from day_abstract import Day


class Day01(Day):
    def __init__(self, input_file):
        super().__init__(input_file);

    def run(self) -> int:
        input = self.input_list(int)
        total = 0
        for i in range(1, len(input)):
            total += input[i] > input[i - 1]
        return total
