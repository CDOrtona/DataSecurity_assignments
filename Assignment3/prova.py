import random
def square_and_multiply(base, exp, mod):
    exp_list = [int(i) for i in bin(exp)[2:]]
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
            return 0
    return 1


def extended_eucledian_algorithm(a, m):
    ''' Documentation '''
    # Code here
    r0, r1 = m,a 
    s0,s1,t0,t1 = 0,1,1,0

    while True:
        r2 = r0 % r1
        q = (r0 - r2)/r1
        s2 = s0-q*s1
        t2 = t0-q*t1
        if r2 == 0:
            break
        r0,r1 = r1,r2
        t0,t1 = t1,t2
        s0,s1 = s1,s2
    
    if r1 == 1:
        return s1
    else:
        return "ERRORE"


print(extended_eucledian_algorithm(5, 5568))