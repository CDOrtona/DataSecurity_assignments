from random import randint


def square_and_multiply(base, exp, mod):
    exp_list = [int(i) for i in bin(exp)[2:]]
    y = 1

    for i in exp_list:
        y = pow(y, 2, mod)
        if i == 1:
            y = (y * base) % mod

    return y


# p = q*2^r+1
# q1 = p-1 = q*2^r
# q is odd hence the module 2 of q will always be different than 0
def _comp_coeff(number):
    r, q1 = 0, number - 1
    while q1 % 2 == 0:
        r += 1
        q1 //= 2
    return q1, r


def miller_rabin_test(prime_num, num_trials=None):
    q, r = _comp_coeff(prime_num)
    for _ in range(num_trials):
        x = randint(2, prime_num - 2)
        y = square_and_multiply(x, q, prime_num)
        if y == 1 or y == prime_num - 1:
            continue
        for _ in range(r):
            y = square_and_multiply(y, 2, prime_num)
            if y == prime_num - 1:
                break
        else:
            return False
    return True


def extended_euclidean_algorithm(a, m):
    (r0, r1) = (m, a)
    (s0, s1, t0, t1) = (0, 1, 1, 0)

    while True:
        r2 = r0 % r1
        q = (r0 - r2) // r1
        (s0, s1) = (s1, s0 - q * s1)
        (t0, t1) = (t1, t0 - q * t1)
        if r2 == 0:
            break
        else:
            r0, r1 = r1, r2

    if r1 == 1:
        if s0 < 0:
            # gcd(a,m) = sign(s)a*s + sign(t)m*t -> it avoids to have negative 's'
            return int(s0 % m)
        return int(s0)
    else:
        raise ValueError("No modular inverse exists")


def read_bin(file_name):
    with open(file=file_name, mode='rb') as file:
        try:
            bin_file = file.read()
            return bin_file
        except(IOError, OSError):
            return "It appears an error occurred while reading your file"
