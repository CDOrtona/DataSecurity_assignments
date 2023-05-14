from Cryptodome.Cipher import AES
from Cryptodome.Util.Padding import pad, unpad
from matplotlib import pyplot as pl
import numpy as np
from rsa import RSA
from utils import read_bin


def block_cipher():
    key = b'0123456701234567'
    # cipher = AES.new(key, AES.MODE_ECB)
    sender = AES.new(key, AES.MODE_CFB)
    receiver = AES.new(key, AES.MODE_CFB, sender.IV)
    print(f'AES block size -> {AES.block_size}')
    # cipher = AES.new(key, AES.MODE_CFB)
    # cipher = AES.new(key, AES.MODE_CTR)
    plaintextA = b'this is a random message'
    cipher_text = sender.encrypt(pad(plaintextA, AES.block_size))
    print(cipher_text)
    plain_text = unpad(receiver.decrypt(cipher_text), AES.block_size)
    print(plain_text)

    vectorized_im = read_bin('secret_message.bin')

    cipher_im = sender.encrypt(vectorized_im)
    plain_im_unrolled = np.reshape(np.array(list(receiver.decrypt(cipher_im))), (2048, 2912))
    pl.imshow(plain_im_unrolled, cmap='gray')
    pl.show()


def message_exc():
    k_AES = b'0123456701234567'

    Bob = RSA(key_length=128, mrt_trials=1000)
    Alice = RSA(k_pub=Bob.key_pub)

    k_aes_enc = Alice.encrypt(int.from_bytes(k_AES, "big"))
    print(f'length of the encrypted AES key is {type(k_aes_enc)}')

    y = read_bin('ciphertext_AES.bin')

    Bob_AES = AES.new(Bob.decrypt(k_aes_enc).to_bytes(Bob.key_length // 8, "big"), AES.MODE_ECB)
    x = Bob_AES.decrypt(y)

    print(Alice, Bob)
    print(f'---- Plaintext ---- \n {x}')


def test():
    e = 41411
    bin_e = bin(e)[2:0]
    print(bin(e))


if __name__ == "__main__":
    # block_cipher()
    message_exc()
    test()
