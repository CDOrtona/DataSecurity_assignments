import functools
from operator import xor


def bitlist_to_int(bitlist):
    out = 0
    for bit in bitlist:
        out = (out << 1) | bit
    # print(f'bitlist -> {bitlist} , int -> {out}')
    return out


def int_to_bitlist(int_num):
    return list(int(i) for i in bin(int_num)[2:])


def disparity(d_prev):
    str_bit = bin(d_prev)[2:]
    return sum(int(b) for b in str_bit) % 2


def berlekamp_massey(bits):
    m, r, P, Q = 0, 1, 1, 1

    for t in range(len(bits)):
        d_prev = bitlist_to_int(bits[t - m:t + 1]) & P
        d = disparity(d_prev)
        print("disparity ->", d)

        if d == 1:
            if 2 * m <= t:
                R = P  # fix
                P = P ^ (Q << r)  # P xor Q shifted
                Q = R
                m, r = t + 1 - m, 0
            else:
                P = P ^ (Q << r)

        r = r + 1

    linear_complexity = len(int_to_bitlist(P)) - 1

    return P, linear_complexity