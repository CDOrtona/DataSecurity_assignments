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

    ciphertext = utils_substitution.read_ciph(os.path.join("ciphertext_simple.txt"))
    ciph_dist = utils_substitution.ciph_dist(ciphertext)

    rule = utils_substitution.create_mapping(ciph_dist, eng_dist)
    print('alphabet: ', ''.join(rule.values()))
    print('alphabet: ', ''.join(rule.keys()))
          
    cip_sample = ciphertext[:1000]

    plaintext = utils_substitution.substitution_decoding(cip_sample,rule)
    
    # print(cip_sample)
    #supponiamo che vengano correttamente mappate r = e, e = t, y = a perchè sono le 3 che compaiono più di frequente
    #riconosciamo nel testo il formato di una data, poichè abbiamo assunto che la a viene convertita correttamente il primo mese è aprile
    #modifichiamo la rule per farlo matchare
    rule['f'], rule['d'] = 'p' , 'n'
    rule['h'], rule['m'] = 'r', 'h'
    rule['d'], rule['t'] = 'l', 'p'
    print('alphabet: ', ''.join(rule.values()))
    print('alphabet: ', ''.join(rule.keys()))
    plaintext = utils_substitution.substitution_decoding(cip_sample,rule)

    print(plaintext)



    
    

    


if __name__ == "__main__":
    # caesar()
    substitution()








