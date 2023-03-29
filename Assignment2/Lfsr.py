import numpy as np

class Lfsr_class():

    def __init__(self, poly, state=None):
        self.length = max(poly)
        self.poly = [i in poly for i in range(self.length+1)]
        if state is None:
            self.state = [True for _ in range(self.length+1)]
        else:
            self.state = [bool(int(i)) for i in list(bin(state)[2:])]

        self.output = self.state[self.length-1]
        self.feedback = np.bitwise_xor.reduce([a & b for a, b in zip(self.poly[1:], self.state)])
        self.counter = 0

    def __next__(self):
        self.counter += 1
        print(self.state)
        # print(f'type of state {type(self.feedback)}')
        print(f'feedback -> {self.feedback}')
        print(f'output -> {self.output}')
        self.output = self.state[self.length-1]
        self.state = self.feedback + self.state[1:]
        print(self.state[1:])
        self.feedback = np.bitwise_xor.reduce([a & b for a, b in zip(self.poly[1:], self.state)])
        # self.state = self.state >> 1
        return self.output

    def __len__(self):
        return self.length

    def __iter__(self):
        return self
