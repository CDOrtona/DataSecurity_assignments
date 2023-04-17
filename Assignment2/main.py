from Lfsr import Lfsr_class
from itertools import islice
import utils


def print_lfsr(lfsr):
    print(f'{lfsr.state} {lfsr.output} {lfsr.feedback}')


def lfsr_generator():
    poly_list = [3, 1, 0]  # possibile errore di lunghezza poly != state
    state_list = 7

    lfsr = Lfsr_class(poly_list, state_list)

    print('\nstate     b fb')
    for b in islice(lfsr, 7):
        print_lfsr(lfsr)

    full_cycle = lfsr.cycle()
    print(f'\nfull LFSR cycle -> {full_cycle}')

    P, comp = utils.berlekamp_massey(full_cycle)
    print(P, comp)


# ______________ Alternating Step Generator _______________


if __name__ == '__main__':
    # lfsr_generator()
    pass

