import functools
from operator import xor

class Lfsr_class():

    def __init__(self, poly, state=None):
        self.length = max(poly)
        self.poly = [1 if i in poly else 0 for i in range(self.length+1) ]
        print(self.poly)
        if state is None:
            self.state = [1 for _ in range(self.length+1)]
        else:
            self.state = [int(i) for i in list(bin(state)[2:])]

        self.output = self.state[self.length-1]
        self.feedback = functools.reduce(xor, [a & b for a, b in zip(self.poly[1:], self.state)])
        self.counter = 0

    def __next__(self):
        self.counter += 1
        #print(self.state)
        # print(f'type of state {type(self.feedback)}')
        #print(f'feedback -> {self.feedback}')
        #print(f'output -> {self.output}')
        
        self.state.insert(0, self.feedback )
        self.state = self.state[:self.length]
        
        self.output = self.state[self.length-1]
        #print(self.state[1:])
        partial = [a&b for a,b in zip(self.poly[1:],self.state)]
        self.feedback = functools.reduce(xor, partial)
        
        return self.output

    def __len__(self):
        return self.length

    def __iter__(self):
        return self
