import os
import numpy as np
import string
import pickle
import matplotlib.pyplot as plt

SHIFT_EXERCISE = 14
ALPHABET = tuple(string.ascii_lowercase)


# _____________________ utils ___________________

def read_cipher(file_name):
    try:
        with open(file=file_name, mode='r', encoding='utf-8') as file:
            cipher = file.read()
            return cipher
    except (IOError, OSError):
        return "It appears an error occurred while reading your file"


def write_plaintext(plaintext, file_name):
    try:
        with open(file=os.path.join(file_name), mode='w', encoding='utf-8') as file:
            file.write(plaintext)
    except (IOError, OSError):
        return "It appears an error occurred while writing your file"


def read_pickle(file_name):
    with open(file=file_name, mode='rb') as file:
        eng_dist = pickle.load(file)
    return dict(sorted(eng_dist.items(), key=lambda x: x[1], reverse=True))


def plot_me(funs_list):
    fig, ax = plt.subplots(len(funs_list), 1)
    for i, fun in enumerate(funs_list):
        ax[i].bar(fun[0].keys(), fun[0].values())
        ax[i].set(ylabel='frequency', xlabel='letters', title=fun[1])
    fig.tight_layout()
    plt.show()


# _____________________ Caesar Cipher ___________________

def caesar_decoding(ciphertext, shift=0):
    # letters in unicode range from 97 to 122 , space -> 32, comma -> 44
    # NOTE: the shift is equal to 14
    alphabet = tuple(string.ascii_lowercase)
    ciphered_alphabet = alphabet[-shift:] + alphabet[:-shift]
    print(ciphered_alphabet)
    rule = dict(zip(alphabet, ciphered_alphabet))
    print(f'the rule is {rule}')
    plaintext = [rule[letter] if 97 <= ord(letter) <= 127 else letter for letter in ciphertext]
    return ''.join(plaintext)


def caesar():
    file_path = os.path.join('ciphertext_caesar.txt')
    ciphertext = read_cipher(file_path)

    sample_cipher = ciphertext[:27]
    for i in range(len(ALPHABET)):
        print(f"Iteration: {i}")
        print(caesar_decoding(sample_cipher, i))

    complete_plaintext = caesar_decoding(ciphertext, SHIFT_EXERCISE)
    write_plaintext(complete_plaintext, "caesar_plaintext")


# _____________________ Substitution ___________________

def cipher_dist(ciphertext):
    freq = list(ciphertext.lower().count(letter) for letter in ALPHABET)
    prob = freq / np.sum(freq)
    ciph_dist = dict(zip(ALPHABET, prob))
    return dict(sorted(ciph_dist.items(), key=lambda x: x[1], reverse=True))


def substitution_decoding(ciphertext, rule):
    plaintext = [rule[character] if 97 <= ord(character) <= 122 else character for character in ciphertext]
    return ''.join(plaintext)


def substitution():

    ciphertext = read_cipher(os.path.join("ciphertext_simple.txt"))
    ciph_dist = cipher_dist(ciphertext)
    eng_dist = read_pickle(os.path.join("letters-freq.pkl"))

    # print the distribution of the letters in the ciphertext
    for letter, prob in ciph_dist.items():
        print(f'{letter} -> {prob}')

    plot_me([[eng_dist, "English Alphabet Distribution"], [ciph_dist, "Ciphertext Alphabet Distribution"]])

    rule = dict(zip(ciph_dist.keys(), eng_dist.keys()))
    print(f"english_alphabet: {''.join(rule.values())}")
    print(f"cipher_alphabet:  {''.join(rule.keys())}")

    cip_sample = ciphertext[:1000]
    plaintext = substitution_decoding(cip_sample, rule)
    print(plaintext)

    # print(plaintext) supponiamo che vengano correttamente mappate r = e, e = t, y = a perchè sono le 3 che
    # compaiono più di frequente riconosciamo nel testo il formato di una data, poichè abbiamo assunto che la a viene
    # convertita correttamente il primo mese è aprile modifichiamo la rule per farlo matchare
    rule['n'], rule['d'] = 'p', 'f'
    rule['v'], rule['m'] = 'r', 'h'
    rule['h'], rule['t'] = 'l', 'd'

    # mapping supposti corretti -> r = e, e = t, y = a, n = p, v = r, h = l
    # secondo february
    rule['i'], rule['d'] = 'f', 'w'
    rule['c'], rule['b'] = 'u', 'm'

    # biography
    rule['f'], rule['j'] = 'o', 'n'

    # which he published in
    rule['t'], rule['l'] = 'c', 'd'
    rule['b'], rule['l'] = 'd', 'm'

    # shannon is noted for having founded information theory
    rule['e'], rule['j'] = 'n', 't'

    # xoined -> joined
    # organiqations -> organization
    rule['u'], rule['p'] = 'j', 'x'
    rule['k'], rule['g'] = 'z', 'q'

    write_plaintext(substitution_decoding(ciphertext, rule), "substitution_plaintext.txt")


if __name__ == "__main__":
    # caesar()
    substitution()
