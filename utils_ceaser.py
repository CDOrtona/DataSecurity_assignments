import os


def open_cipher(file_name):
    with open(file=file_name, mode='r', encoding='utf-8') as file:
        cipher = file.read()
    return cipher


def write_plaintext(plaintext):
    with open(file=os.path.join("plaintext.txt"), mode='w', encoding='utf-8') as file:
        file.write(plaintext)


def ceaser_decoding(ciphertext, shift=0):
    # string to unicode conversion -> unicode expressed in decimals
    # letters range from 97 to 122 , space -> 32, comma -> 44
    cipher_array = list(ord(letter) for letter in ciphertext)
    # NOTE: we're moving forward hence we got a shift equal to 12. The actual shift is 26-12=14
    for i in range(len(cipher_array)):
        if 97 <= cipher_array[i] <= 122:
            new_letter = cipher_array[i] + shift
            if 97 <= new_letter <= 122:
                cipher_array[i] = new_letter
            else:
                cipher_array[i] = 97 + (new_letter - 122 - 1)

    plaintext = ''.join(list((chr(letter) for letter in cipher_array)))
    # write_plaintext(plaintext)

    return plaintext
