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


# ------------------------------ Alternating Step Generator --------------------------------------------


def _check_seed(seed, lfsr_type):
    if 1 in seed:
        return seed
    else:
        raise ValueError(f'The LFSR {lfsr_type} has its initial state set to 0')


def _bit_to_int(bitlist):
    out = 0
    for bit in bitlist:
        out = (out << 1) | bit
    return out


class AlternatingStepGenerator:
    def __init__(self, seed):

        seed_bin = [int(i) for i in bin(seed)[2:]]

        try:
            self.seed_c = _check_seed(seed_bin[8:], "C")
            self.seed_0 = _check_seed(seed_bin[:5], "0")
            self.seed_1 = _check_seed(seed_bin[5:8], "1")
        except ValueError as err:
            print(err)
            quit()

        self.lfsr_c = Lfsr_class([2, 1, 0], _bit_to_int(self.seed_c))
        self.lfsr_0 = Lfsr_class([5, 2, 0], _bit_to_int(self.seed_0))
        self.lfsr_1 = Lfsr_class([3, 1, 0], _bit_to_int(self.seed_1))

    def __iter__(self):
        return self

    def __next__(self):
        if next(self.lfsr_c):
            bit = next(self.lfsr_1) ^ self.lfsr_0.output
        else:
            bit = self.lfsr_1.output ^ next(self.lfsr_0)

        return bit


# ------------------------------------------ RC4 ---------------------------------------------------------

class RC4:

    def __init__(self, seed, drop=0):
        # initialization of the identity permutation
        self.P = list(range(256))
        t = 0

        for k in range(256):
            t = (t + self.P[k] + seed[k % len(seed)]) % 256
            self.P[k], self.P[t] = self.P[t], self.P[k]

        # variables for the PGRA
        self.i = 0
        self.j = 0

        # It'll drop the first n values generated
        for _ in range(drop):
            self.__next__()

    def __iter__(self):
        return self

    def __next__(self):
        self.i = (self.i + 1) % 256
        self.j = (self.j + self.P[self.i]) % 256
        self.P[self.i], self.P[self.j] = self.P[self.j], self.P[self.i]
        byte = self.P[(self.P[self.i] + self.P[self.j]) % 256]
        return byte

# ------------------------------- Bonus Task -----------------------------------------


class StreamCipher:

    def __init__(self, key, prng, **kwargs):
        self.prng = prng(key, **kwargs)

    def encrypt(self, plaintext):
        return self._crypting(plaintext)

    def decrypt(self, ciphertext):
        return self._crypting(ciphertext)

    def _crypting(self, text):
        return [a ^ b for a, b in zip(text, self.prng)]
