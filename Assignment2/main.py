from Lfsr import Lfsr_class
from itertools import islice


def print_lfsr(lfsr):
    print(f'{lfsr.state} {lfsr.output} {lfsr.feedback}')


if __name__ == '__main__':

    poly_list = [3, 1, 0]
    state_list = 7

    lfsr = Lfsr_class(poly_list, state_list)

    print('\nstate     b fb')
    for b in islice(lfsr, 7):
        print_lfsr(lfsr)

    full_cycle = lfsr.cycle()
    print(f'\nfull LFSR cycle -> {full_cycle}')

    print(lfsr)
