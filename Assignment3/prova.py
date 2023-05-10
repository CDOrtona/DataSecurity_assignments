import random
import math

def square_and_multiply(base, exp, mod):
    exp_list = [int(i) for i in bin(abs(exp))[2:]]
    y = 1

    for i in exp_list:
        y = pow(y,2,mod)
        if i == 1:
            y = (y*base) % mod

    return y

def comp_coeff(number):
    r, q = 0, number - 1
    while q % 2 == 0:
        r += 1
        q //= 2
    return q,r

def miller_rabin_test(number, num_trials=None):
    q, r = comp_coeff(number)
    for _ in range(num_trials):
        x = random.randint(2, number-2)
        y = square_and_multiply(x, q, number)
        if (y == 1 or y == number-1):
            continue
        for _ in range(r):
            y = pow(y, 2, number)
            if y == number - 1:
                break
        else:
            return False
    return True

print(miller_rabin_test(0x1083e935648922e73, 100000))



def extended_eucledian_algorithm(a, m):
    ''' Documentation '''
    # Code here
    r0, r1 = m,a
    s0,s1,t0,t1 = 0,1,1,0

    while True:
        r2 = r0 % r1
        q = (r0 - r2)//r1
        s2 = s0-q*s1
        t2 = t0-q*t1
        if r2 == 0:
            break
        r0,r1 = r1,r2
        t0,t1 = t1,t2
        s0,s1 = s1,s2

    if r1 == 1:
        if s1 < 0:
            return int((m - (-s1)) % m)
        return int(s1%m)
    else:
        raise ValueError("No modular inverse exists")




class RSA():

    def __init__(self, key_length=128, k_pub=None, mrt_trials=None):
        ''' Documentation '''
        # Code here
        if k_pub != None:
            self.key_pub = k_pub
        else:

            self.key_pub, totien = self._compute_key(mrt_trials, key_length)
            self.key_priv = extended_eucledian_algorithm(self.key_pub[1], totien) #unpacking operator
            print("key priv " + str(self.key_priv))





    def _compute_key(self, trials, key_length = 128):
        # p = self._sample_prime_number(key_length, trials)
        # q = self._sample_prime_number(key_length, trials)
        # print("P", p)
        # print("Q", q)
        p, q = 17,17
        n = q*p
        print(n)
        # p = 59
        # q = 97
        # n = q*p

        totient = (p-1)*(q-1)
        print("totient", totient)

        while True:
            e = random.randint(2, totient-1)
            if math.gcd(e, totient) == 1:
                break

        print("e", e)
        
        e = 57

        return (n,e), totient



    # mandatory methods:

    def _sample_prime_number(self, length, mrt_trials=None):
        ''' Documentation '''
        # Code here
        while True:
            number = random.randint(2**(length/2) , 2**(length/2 + 1))
            if miller_rabin_test(number, mrt_trials):
                break
        return number

    def decrypt(self, y):
        ''' Documentation '''
        # Code here
        return square_and_multiply(y, self.key_priv, self.key_pub[0])

    def encrypt(self, x):
        ''' Documentation '''
        # Code here
        return square_and_multiply(x, self.key_pub[1], self.key_pub[0])

Bob = RSA(key_length = 8, mrt_trials=1000)
Alice = RSA(k_pub=Bob.key_pub)

x = 9
y = Alice.encrypt(x)
print("y",y)
x = Bob.decrypt(y)
print("result", x)






