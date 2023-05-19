import math
import numpy as np


class BigInt:

    def _from_num_to_array(self, number, value):
        if isinstance(number, bytes):
            number = int.from_bytes(number, "big")

        arr = np.array([(number >> ((value - i - 1) * 64)) & 0xFFFFFFFFFFFFFFFF for i in range(value)], dtype=np.uint64)
        print(f'array is {arr}')
        return arr

    def __init__(self, value=None, ndigit=None):
        if ndigit is None:
            if isinstance(value, np.ndarray):
                ndigit = value.size
            else:
                ndigit = math.ceil(len(bin(value)[2:]) / 64)

        if not isinstance(value, np.ndarray):
            self.values = self._from_num_to_array(value, ndigit)
        else:
            self.values = value

    def long_sum(self, a, b):
        # somma da luogo a risultato che al più è una digit in più del più lungo dei due, padding dei due per
        # allinearli.
        print(a, '\n', b)
        sum_result = np.zeros(max(len(a), len(b)) + 1, dtype=np.uint64)
        a_pad = np.pad(a, (sum_result.size - len(a), 0))
        b_pad = np.pad(b, (sum_result.size - len(b), 0))
        carry = 0

        for i in range(sum_result.size - 1, -1, -1):
            sum_result[i] = a_pad[i] + b_pad[i] + carry
            if sum_result[i] < min(a_pad[i], b_pad[i]):
                carry = 1
            else:
                carry = 0

        c = BigInt(sum_result)

        return c

    def long_mul(self, x, y):
        # print(type(x), type(y))
        mul_result = np.zeros(len(x) + len(y) + 1, dtype=np.uint64)
        temp_mul = np.zeros_like(mul_result, dtype=np.uint64)
        for j in range(0, len(y), 1):
            print(f'j = {j}')
            temp_mul += np.roll(mul_result, -j)
            for i in range(0, len(x), 1):
                if y[len(y) - 1 - j] > 0 and x[len(x) -1 -i] > 2**64 / y[len(y) - 1 - j]:
                    print(x[len(x) - 1 - i], y[len(y) - 1 - j])
                    print(True)
                    mul_result[mul_result.size - 2 - i] = 1
                    mul_result[mul_result.size - 1 - i] += x[len(x) - 1 - i] * y[len(y) - 1 - j]
                    print(f'temp_mul = {temp_mul}')
                    print(f'mul_result = {mul_result}')
                else:
                    print(x[len(x) - 1 - i], y[len(y) - 1 - j])
                    mul_result[mul_result.size - 1 - i] += x[len(x) - 1 - i] * y[len(y) - 1 - j]
                    print(f'temp_mul = {temp_mul}')
                    print(f'mul_result = {mul_result}')

        return self.long_sum(temp_mul, mul_result)

    def __add__(self, x):
        return self.long_sum(self, x)  ##### CHANGE VALUESSS

    def __str__(self):
        return str(self.values)

    def __mul__(self, x):
        return self.long_mul(self, x)

    def __getitem__(self, item):
        return self.values[item]

    def __len__(self):
        return self.values.size


# a = BigInt(18446744073709551616)
# b = BigInt(5 * 2 ** 64 + 1)
#
# c = a + b
# print(c)

# a = BigInt(18446744073709551615) # 2^64 -1
# b = BigInt(2)
# a = BigInt(3*2**64+1)
# b = BigInt(2*2**64)
# a = BigInt(3*2**64+2**64-1)
# b = BigInt(2*2**64+2)
# a = BigInt(2*2**64 + 2) # questo funziona
# b = BigInt(2**64-1)
a = BigInt(2**64-1)
b = BigInt(2)
c = a * b

d = BigInt((2**64-1)*(2))
print(f'd is {d}')

print(f'c = {c}')

