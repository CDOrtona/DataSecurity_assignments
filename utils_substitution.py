import pickle
import string
import numpy as np 

def read_pickle(file_name):
    with open(file=file_name, mode='rb') as file:
        eng_dist = pickle.load(file)
    return dict(sorted(eng_dist.items(), key = lambda x:x[1],reverse=True)) # items ogni coppia diventa lista, key = lamba per ognuno prende il value
    

def ciph_dist(ciphertext):
    alphabet = tuple(string.ascii_lowercase)
    freq = list(ciphertext.lower().count(letter) for letter in alphabet)
    prob = freq/np.sum(freq)
    cipher_dist = dict(zip(alphabet, prob))
    return dict(sorted(cipher_dist.items(), key = lambda x:x[1],reverse=True))
    

def read_ciph(file_name):
    with open(file = file_name, mode='r', encoding='utf-8' ) as file:
        ciphertext = file.read()
    return ciphertext

def create_mapping(cip_dis, eng_dis):
    return dict(zip(cip_dis.keys() , eng_dis.keys()))

def substitution_decoding(ciphertext, rule):
    alphabet = tuple(string.ascii_lowercase)
    plaintext = ''
    for char in ciphertext:
        if char in alphabet:
            plaintext = plaintext + rule[char]
        else: 
            plaintext = plaintext + char

    return plaintext

