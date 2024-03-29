from math import log2
from math import ceil


def bits_to_integer(bits):
    '''
    Given a list of bits its integer representation is generated
    EX: [1, 0, 1, 1] -->  11 (0b1011)
    ----------
    bits: list,
        the list of bits (each represented with an integer 0/1 or a bool)

    Return
    ------
    int,
        integer having the binary representation defined by the list
    '''
    
    integer = 0
    
    for bit in bits:
        integer = (integer << 1) ^ bit
        
    return integer


def bits_to_bytes(bits, num_bytes=None, byteorder='big'):
    '''
    Converts a list of bits into bytes
    EX: [1, 0, 1, 1] -->  11 (0b1011)
    ----------
    bits: list,
        the list of bits (each represented with an integer 0/1 or a bool)
    num_bytes: int, optional
        the number of bytes to use for the representation
        (when None the least ammout of bytes is used)  
    byteorder: str, optional
        the order of the bytes
        (defualt is big)

    Return
    ------
    bytes,
        byte string defined by the integer
    '''
    
    if num_bytes is None:
        num_bytes = ceil(len(bits) / 8)
        
    bytestream = bits_to_integer(bits).to_bytes(num_bytes, byteorder)
    return bytestream


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


def integer_to_bits(integer, nbit=None):
    '''
    Given an integer, it generates the corresponding sequence of bits
    EX:  11 (0b1011) --> [1, 0, 1, 1]
    ----------
    integer: int,
        integer to convert into a list of bits,
    nbit: int, optional (default None)
        length of the output sequence of bits.
        If None the length is ceil(log2(integer)) 

    Return
    ------
    list of bools,
        output bit sequence
    '''
    
    if nbit is None:
        nbit = max(1, ceil(log2(integer + 1))) 
        
    bits = []
    for i in range(nbit):
        bits.append((integer & (1 << i)) >> i)
    return bits[::-1]


def bytes_to_bits(bytestream):
    '''
    Given a byte string, it generates the corresponding sequence of bits
    EX:  b'a' (0x61) --> [0, 1, 1, 0, 0, 0, 0, 1]
    ----------
    bytestream: bytes,
        byte string to convert into a list of bits,

    Return
    ------
    list of bool,
        output bit sequence with lenght 8*len(bytestream)
    ''' 
    
    integer = int.from_bytes(bytestream, byteorder='big')
    bits = integer_to_bits(integer, nbit=8*len(bytestream))
    
    return bits
    


