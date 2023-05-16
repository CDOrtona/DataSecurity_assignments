import math
import numpy as np

class BigInt:

    def _from_num_to_array(self,number, value):
        if isinstance(number, bytes):
            number = int.from_bytes(number, "big")

        arr = np.array([(number >> ((value - i - 1) * 64)) & 0xFFFFFFFFFFFFFFFF for i in range(value)], dtype=np.uint64)

        return arr
    
    
    def __init__(self, value = None, ndigit = None):

        if ndigit is None:
            if isinstance(value, np.ndarray):
                ndigit = value.size
            elif ( value is None):
                ndigit = 0
            else:
                ndigit = math.ceil(len(bin(value)[2:])/64 )

        if not isinstance(value, np.ndarray):
            self.values = self._from_num_to_array(value, ndigit)
        elif ( value is None):
            self.values = np.array([], dtype=np.uint64)
        else:
            self.values = value

    def long_sum(self, a, b):
        sum_result = np.zeros(max(a.size, b.size) + 1, dtype=np.uint64)
        carry = 0
        for i in range(len(x) - 1, -1, -1):
            temp_sum = int(x[i]) + int(y[i]) + carry
            sum_result[i] = temp_sum % 2 ** 64
            carry = temp_sum // 2 ** 64

        return sum_result
    
    
    def __add__(self, x):
        return self.long_sum(self.values, x.values)
    
    def __str__(self):
        return str(self.values)
    
    def long_mul(self,x, valuex,y, valuey):
    
        mul_result = np.zeros(valuex + valuey, dtype=np.uint64)
        for i in range(len(x)-1, -1, -1):
            new_sum =np.zeros_like(mul_result, dtype=np.uint64)
            for j in range(len(y)-1,-1,-1):
                new_sum[len(new_sum) + i - len(x)] = int(x[i])*int(y[j]) % 2**64
                new_sum[len(new_sum) + i - len(x) - 1] = int(x[i])*int(y[j]) // 2**64
                mul_result = mul_result + new_sum
        
        
    
        return mul_result
    
    def __mul__(self, x):
        return self.long_mul(self.values, self.values.size, x.values, x.values.size)


a = BigInt(2**64)
print(a)
b = BigInt(2)
print(b)

c = a+b
print(c)

    