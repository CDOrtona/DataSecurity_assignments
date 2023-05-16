import random
from utils import extended_euclidean_algorithm, miller_rabin_test, square_and_multiply


class RSA:

    def __init__(self, key_length=128, k_pub=None, mrt_trials=None):
        self.key_length = key_length
        if k_pub is not None:
            self.role = 'SENDER'
            self.key_pub = k_pub
        else:
            self.role = 'RECEIVER'
            self.key_pub, self.param = self._compute_key(mrt_trials, key_length)
            try:
                self.key_priv = extended_euclidean_algorithm(self.key_pub[1], self.param[2])
            except ValueError as err:
                print(err)

    def _compute_key(self, trials, key_length=128):
        p = self._sample_prime_number(key_length, trials)
        q = self._sample_prime_number(key_length, trials)
        n = q * p

        # totient is computed as a factorization of prime numbers
        # it is wrong to choose two same prime numbers because it reduces the security of the system
        totient = (p - 1) * (q - 1) if p != q else p * (p - 1)

        # e is found such that gcd(e,m) = 1, this means that e must be prime
        # 65537 = 2^16 + 1 is commonly used as a public exponent in the RSA cryptosystem
        # it is big enough to be secure and it has a low hamming weight hence it's not
        # computationally demanding to compute
        e = 65537

        return (n, e), (p, q, totient)

    def _sample_prime_number(self, length, mrt_trials=None):

        while True:
            # n > x where x is the length of the plaintext, which in this case is the AES key
            # the AES key is 128-bit long, hence the chosen interval is: (2^64, 2^65 -1) -> n is long 129-bit
            # NOTE: cryptographically secure pseudo random generator?
            number = random.randint(2 ** (length / 2), 2 ** (length / 2 + 1) - 1)
            # since e=65537 I have to pick numbers which are not congruent to 1 modulo 65537
            # phi(n)=(p-1)(q-1) and gcd(e,phi(n))=1 if this last relation is not satisfied: gcd(e,p-1)=k
            # and we would have p-1 == 0 mod(e) which means p-1 is a multiple of e and it would mean that no module
            # inverse exists because p-1 and e are not coprime
            # basically I have to check whether the prime number found is divisible by the public exponent or not
            if miller_rabin_test(number, mrt_trials) and (lambda x: False if x % 65537 == 0 else True)(number):
                break
        return number

    def decrypt(self, y):

        return square_and_multiply(y, self.key_priv, self.key_pub[0])

    def encrypt(self, x):

        return square_and_multiply(x, self.key_pub[1], self.key_pub[0])

    def __str__(self):
        if self.role == 'RECEIVER':
            return f'------------------ RSA INFO ---------------- \n' \
                   f'Role: {self.role} \n' \
                   f'p, q, totient -> {self.param[0], self.param[1], self.param[2]} \n' \
                   f'Public key (n, e) -> {self.key_pub} \n' \
                   f'Private Key (d) -> {self.key_priv}'
        else:
            return f'------------------ RSA INFO ---------------- \n' \
                   f'Role: {self.role} \n' \
                   f'Public key (n, e) -> {self.key_pub} \n'

    def __repr__(self):
        if self.role == 'RECEIVER':
            return f'------------------ RSA INFO ---------------- \n' \
                   f'Role: {self.role} \n' \
                   f'p, q, totient -> {self.param[0], self.param[1], self.param[2]} \n' \
                   f'Public key (n, e) -> {self.key_pub} \n' \
                   f'Private Key (d) -> {self.key_priv}'
        else:
            return f'------------------ RSA INFO ---------------- \n' \
                   f'Role: {self.role} \n' \
                   f'Public key (n, e) -> {self.key_pub} \n'
