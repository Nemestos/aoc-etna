from abc import ABC, abstractmethod


class Day(ABC):
    @abstractmethod
    def __init__(self, input_file):
        self.input = input_file

    @abstractmethod
    def run(self)->int:
        print("day")
    
    def get_input(self):
        return open(self.input, 'r')

    def input_list(self,func=None):
        lines = self.get_input().readlines()
        if func is not None:
            return list(map(func,lines))
        return lines
