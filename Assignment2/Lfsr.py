import functools    
from operator import xor


class Lfsr_class:

    def __init__(self, poly, state=None):
        # self.counter = 0
        self._poly = poly
        self._state = state
        self.length = max(poly)
        self.poly = [1 if i in poly else 0 for i in range(self.length + 1)]

        if state is None:
            self.state = [1 for _ in range(self.length + 1)]
        else:
            self.state = [int(i) for i in list(bin(state)[2:])]
            print(f'Initial state -> {self.state}')

        self.output = self.state[self.length - 1]
        self.feedback = functools.reduce(xor, [a & b for a, b in zip(self.poly[1:], self.state)])

    def __len__(self):
        return self.length

    def __iter__(self):
        return self

    # this runs every single step of a N length LSFR
    def run_steps(self, n=0):
        return [next(self) for _ in range(n)]

    # this executes a full LFSR cycle
    # if length is 3, then it performs 2^3-1 steps
    def cycle(self, state=None):
        if state is not None:
            self.state = state
        return self.run_steps(2 ** (len(self)) - 1)

    def __next__(self):
        # self.counter += 1
        self.state.insert(0, self.feedback)
        self.state = self.state[:self.length]
        self.output = self.state[self.length - 1]
        self.feedback = functools.reduce(xor, [a & b for a, b in zip(self.poly[1:], self.state)])

        return self.output

    def __str__(self):
        poly_list = [f'x^{d}' for d in self._poly]
        poly = "+".join(poly_list)
        string = f'\nLFSR INFO:' \
                 f'\nPoly: {poly} ' \
                 f'\nState: {hex(self._state)}'
        return string

    def __repr__(self):
        poly_list = [f'x^{d}' for d in self._poly]
        poly = "+".join(poly_list)
        string = f'\nPoly: {poly} \nState: {hex(self._state)}'
        return string




class AlternatingStepGenerator(): 
    ''' Documentation '''
    
    def __init__(self, seed):
        ''' Documentation '''
        seed_bin = [int(i) for i in bin(seed)[2:]] #da implementare RISE AN ERROR

        seed_c = seed_bin[8:]
        seed_0 = seed_bin[:5]
        seed_1 = seed_bin[5:8]        

        self.lfsr_c = Lfsr_class([2,1,0], self.bit_to_int(seed_c))
        self.lfsr_0 = Lfsr_class([5,2,0], self.bit_to_int(seed_0))
        self.lfsr_1 = Lfsr_class([3,1,0], self.bit_to_int(seed_1))


        
    def __iter__(self):
        return self
    
    def __next__(self):
        ''' Documentation '''
        # Code here
        if next(self.lfsr_c):
            bit = next(self.lfsr_1)^self.lfsr_0.output
        else:
            bit = self.lfsr_1.output^next(self.lfsr_0)


        return bit
    
    def bit_to_int(self,    bitlist):
        out=0
        for bit in bitlist:
            out = (out << 1) | bit
        return out
    
    def __str__(self) :
        print

    

