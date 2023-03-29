from Lfsr import Lfsr_class
from itertools import islice

if __name__ == '__main__':

    # implement a descending order algorithm for the poly
    poly_list = [3, 1, 0]
    state_list = 7

    lfsr = Lfsr_class(poly_list, state_list)
    # print(lfsr.poly, lfsr.state, lfsr.length)


    def print_lfsr(lfsr):
        print(f'{lfsr.state} {lfsr.length} {lfsr.output} {lfsr.feedback}')


    for b in islice(lfsr, 7):
        print(lfsr.counter)
        # print_lfsr(lfsr)
        pass



    # a = [True, True, False]
    # b = [True, True, False]
    # c = [a & b for a, b in zip(a, b)]
    # print(bool(c))
    # print(c)

