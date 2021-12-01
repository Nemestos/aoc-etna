from abc import ABC, abstractmethod


class Day(ABC):
    @abstractmethod
    def __init__(self, input_file):
        self.input = input_file

    @abstractmethod
    def run(self):
        print("day")
    
    def get_input(self):
        return open(self.input, 'r')
