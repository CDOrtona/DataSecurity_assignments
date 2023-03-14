import numpy as np
import os
import utils_ceaser
import utils_substitution

NUM_LETTERS = 26
SHIFT_EXERCISE = 12


def caesar():
    file_path = os.path.join('ciphertext_caesar.txt')
    ciphertext = utils_ceaser.open_cipher(file_path)

    sample_cipher = ciphertext[:27]
    for i in range(NUM_LETTERS - 1):
        print(f"Iteration: {i + 1}")
        print(utils_ceaser.ceaser_decoding(sample_cipher, i + 1))

    complete_plaintext = utils_ceaser.ceaser_decoding(ciphertext, SHIFT_EXERCISE)
    utils_ceaser.write_plaintext(complete_plaintext)


def substitution():
    eng_dist = utils_substitution.read_pickle(os.path.join("letters-freq.pkl"))
    print(eng_dist)


if __name__ == "__main__":
    # caesar()
    substitution()








