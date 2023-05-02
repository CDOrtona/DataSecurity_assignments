from Cryptodome.Cipher import AES
from Cryptodome.Util.Padding import pad, unpad
from matplotlib import pyplot as pl
import numpy as np


def block_cipher():
    key = b'0123456701234567'
    # cipher = AES.new(key, AES.MODE_ECB)
    sender = AES.new(key, AES.MODE_CBC)
    receiver = AES.new(key, AES.MODE_CBC, sender.IV)
    # cipher = AES.new(key, AES.MODE_CFB)
    # cipher = AES.new(key, AES.MODE_CTR)
    plaintextA = b'this is a random message'
    cipher_text = sender.encrypt(pad(plaintextA, AES.block_size))
    print(cipher_text)
    plain_text = unpad(receiver.decrypt(cipher_text), AES.block_size)
    print(plain_text)

    with open(file='secret_message.bin', mode='rb') as f:
        vectorized_im = f.read()

    cipher_im = sender.encrypt(vectorized_im)
    plain_im_unrolled = np.reshape(np.array(list(receiver.decrypt(cipher_im))), (2048, 2912))
    pl.imshow(plain_im_unrolled, cmap='gray')
    pl.show()


if __name__ == "__main__":
    block_cipher()

