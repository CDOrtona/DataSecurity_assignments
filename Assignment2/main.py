from Lfsr import Lfsr_class
from Lfsr import AlternatingStepGenerator
from Lfsr import RC4
from itertools import islice
import utils


def print_lfsr(lfsr):
    print(f'{lfsr.state} {lfsr.output} {lfsr.feedback}')


def lfsr_generator():
    poly_list = [3, 1, 0]  # possibile errore di lunghezza poly != state
    state_list = 7

    lfsr = Lfsr_class(poly_list, state_list)

    print('\nstate     b fb')
    for _ in islice(lfsr, 7):
        print_lfsr(lfsr)

    full_cycle = lfsr.cycle()
    print(f'\nfull LFSR cycle -> {full_cycle}')

    P, comp = utils.berlekamp_massey(full_cycle)
    # NOTE: implement a way to print the poly expanded
    print(f'Poly: {P}, linear complexity: {comp}')


def Alternating_step():
    SEED = 0x3FF
    CIPHERTEXT_ALT_STEP = (
        b'Y\xea\xfc\xc2\x8c\x17p{\x1f8\xbf,N\\\xf8\x97\xeb\x99#\'#\xf3\x1cY\xfd'
        b'\x82\xe9\xbe\xc2\xeb\x16H\xd0Q\xd5\xa8Y\x8e\x8b\\\xeb\x8d\xe1\xea\xf5'
        b'\x83\xb0\xe7\xee\xf2\\\xear\x848l\xe2\xb2\x06ov%\xdb\x08\x13\xf2qy\xf6'
        b'}\xfdO\xebG{\xaa\xaf\xbaP\xc1\x98c\x19\xdc5\xf3\x00P_\x0e\x8b\xe9\xa5$'
        b'\xaf,7\x99G\xe5\x89f\xd5o\xd9s\xd4\x10;\xf4\x10\x1a\x84]\xf6>\xd9J\x86'
        b'\xb2/%\x86\x92\xdc3f\x1d\x15\xa0\xa7K1*\xa0\xaa\x88+x\xb9\xa9#Ie)\xf97'
        b'\x05\xf1\x1b\x02~\xeac\xd0\xeb\x0bv+\xd2Y\xb1\xbd\x1d6!\xde\xd9\x9de'
        b'\x05\xb3\xf30\x14\xfd\xa7s\xa9\xce\xad]\x01W\x0b\x9a\xb6\x03\x8e^J\xbf'
        b'\x01\xe4\xb6\xa0\x83\xbej\xb6\xda\xca\xa3J\xd78~1\xaf/t\x1eL\x93\x19J'
        b'\xb18Bm\x7f\xddZ\xa8L\xbd\xb1\x84,\x04\xc7\x0b,\x11\xce}\xed\x06\x06XZ'
        b'\xaf\xcf\xaa-\xaf\xad"\x87\xd3\xf8\xc2\xf7\xd3\x1bM}\xb9\x00)\xb1\x9a'
        b'\x06\xcdU\xedV\xd7\x03\x90\xed;>\xc5\xd7\xff\xa0qZ\x94\xf3\xb6\x1b9v'
        b'\xfa\xfa\xf1x}\xd9\xf3\x7fm\xe4 \xe0"G\xe0O*C%p\xd7yYS&\xd9{\xec\xe9'
        b'=46\xfbH\xcc#\x0f\xe8\xf78H\xcc *\xb8\xd8\xe35\xda\x03>\xc5\xf0\x1a'
        b'OCZ\xfc\x11\xbd\xf7\xb0\xc9\xb2!\xfe\xd8\xc7\x8e\x1c\xc3:\x7fb\xdd9wZ'
        b'\xad\xca\\\x83\xf9>Fx\x1dQ\x1d\x9a\x92\xdb\xc1\x8b+\x19\xdfDK\x93\xd7M'
        b'\xe7Cg\xdbP\xa6\x99\xe5`\xae\xed6E\xcf\xe3\xc2\xb5\xee\x80\x14D+@5\xb2'
        b'\xde\x02\xdb\x01\x9b\xd9\x90<\x00\xe6\n=\x98\xf6\xe9\xb7\x14\x93\x95'
        b'\xc8\xf7YX!\xe2\x830<q\x9b\xed\x034\xa0\x0c|(\x05%h3\x87dN\x160zN\''
        b'\x8ev\xe4\xe0\xb0q\x02\xb1\x10\xa0\x90\x06\xf42SSV4nl\xf4\xd8\xe1\xc3S'
        b'?\x89\xe5\x80\x11X\x1f\xfe-"\xed\xb4D\xb6a\xa3\xdd\xc8\xca\t\xfcrg\x0e'
        b'\xfa|X\x16\x82\xc2\xdb\x86\xfd=\x07cK\x15?\x98\xd3\xf8\xda\xcb\x0c\x0e'
        b'\x84\\\x9c\x84\x87\xd1\xa5P\xab\xcd;')

    alt_gen = AlternatingStepGenerator(SEED)

    # ciphertext expressed as a list of integers, where each integer is a byte
    cipher_list_int = utils.bytes_to_bits(CIPHERTEXT_ALT_STEP)
    plaintext = utils.bits_to_bytes([a ^ b for a, b in zip(cipher_list_int, alt_gen)])
    print(plaintext)


def RC4_dec():
    key = b"0123456789ABCDEF"
    # bytestream formed of integers
    ciphertext = (
        b"\x0f\x9e\xec\xc3\x0f\xeck\xa5\xc9\xd4\xd4\xb81\xf0\xd5[\x93"
        b"\xbc\xdaY^\x0e\xc1'\xdb\x1eP\xc0uD\xeb\x91E]\x15\xcf\x85\x07%"
        b"\x97\xffl\xf1\xbb\xe1*\xa0\xee\xd3\x94\x17\xb0|e\x93h\xd7\xc5"
        b"\xc3tT\x84\xee%\xcb\x15\r\xc4\xe8\n\xf2\xd0.\xec\xc6\xe1-\xb4"
        b"\x8b\x9a\x14\x823k\xab?\x8b\x9c\xaas\xa1#\xb8\xb2\xceh\xb5\x8b"
        b"'\x90B}C\x80~\x8cr\xde\xc9\xe2\x17\xe45\xb9\x10\x94\xd4\x0eRJ"
        b"\x0fr&\xe7\xe3P\xbfz\xecIA\x94\xe60\xa8{_\x03\xc7\x91\xcf\xc6"
        b"\x04\xfc\x8d\x86-E\x13\xba\x13i\x17;\xd7\x8e \xa5\xe6\xa5uR\n"
        b"89z\xe2YZ!e\x0f,s\x9a\xacN\xab\xc7\xcaOO\x81\xe06\x03\xac7\x9b"
        b",%\xf7\x9d(\xde\x0b\xc3\xbf\xbe7\xc7<\xf4r\x0eLz\xd8\xe5b\xa0n"
        b"\x11f\xfe\xca+RNnL\xef+\x1b\x1c\x0b\x8a\xb6M\xbdU\xd6\x1c\x9cn"
        b"\t\x8aX>B9\xa4\xf7\xd7jS\xa3\xfd\xeb=\xeeY\xbf\x8dG\xab\xc6"
        b"\x08 \xfba\x90\xdbla\xbf\xf0\x9c\x1a\xa0\xcb\x9a\x7f\x88X\x1dV"
        b"\xd2'\xba\x1b\x16l\xc3vx\xddqU\xf72@\x86>A\xe6b\x050Y\xed\x8bJ"
        b"!\xe0\x80I\xa4X\x9e\xd6^\x126\x99\x93\xa3(\xc5\xf0\xbd\xdei\xcb"
        b"\xdc5\xf58\xda\xa5\x96\xb9!5>\xdbJ\xd4\xef\xe1\x0e\xfeo\x97`"
        b"\xd7[\x18\t\xf4/DV\xdd\xe8~#\xbd\xfd{B\xacC=\xa9\xd5\xbb\xdbH"
    )
    drop = 3072

    RC4_key = RC4(key, drop)
    plaintext = [chr(a ^ b) for a, b in zip(RC4_key, ciphertext)]
    print("".join(plaintext))


if __name__ == '__main__':
    lfsr_generator()
    Alternating_step()
    RC4_dec()
