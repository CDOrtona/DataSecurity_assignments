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
        # somma da luogo a risultato che al più è una digit in più del più lungo dei due, padding dei due per allinearli. 
        sum_result = np.zeros( max(a.size, b.size) + 1, dtype=np.uint64)
        a_pad = np.pad(a, (sum_result.size - a.size,0))
        b_pad = np.pad(b, (sum_result.size - b.size,0))
        carry = 0

        for i in range(sum_result.size - 1, -1, -1):
            sum_result[i] = a_pad[i] + b_pad[i] + carry
            carry = 1 if sum_result[i] < min(a_pad[i], b_pad[i]) else 0
        
        c = BigInt(sum_result)
    
        return c
    
    
    def __add__(self, x):
        return self.long_sum(self.values, x.values)
    
    def __str__(self):
        return str(self.values)
    
    def long_mul(self,x, valuex,y, valuey):
        mask_down = np.uint64(0x00000000FFFFFFFF)
        mask_up = np.uint64(0xFFFFFFFF00000000)
        carry = 0

        mul_result = np.zeros(valuex + valuey, dtype=np.uint64)
        for i in range(len(x)-1, -1, -1):
            new_sum =np.zeros_like(mul_result, dtype=np.uint64)
            print('x', x[i])
            
            for j in range(len(y)-1,-1,-1):
                print("j is", j)
                print('y', y[j])
                print("here")
                # new_sum[i+j - len(new_sum)] = (np.bitwise_and(x[i], mask_up))*(np.bitwise_and(y[j], mask_down)) + ((np.bitwise_and(x[i], mask_down))*(np.bitwise_and(y[j], mask_up))) >> np.uint64(32) + ((np.bitwise_and(x[i], mask_up))*(np.bitwise_and(y[j], mask_down)))>> np.uint64(32) 
                # new_sum[1+i+j - len(new_sum)] = (np.bitwise_and(x[i], mask_up))*(np.bitwise_and(y[j], mask_down)) + ((np.bitwise_and(x[i], mask_down))*(np.bitwise_and(y[j], mask_up)))>> np.uint64(32) + ((np.bitwise_and(x[i], mask_up))*(np.bitwise_and(y[j], mask_down)))>> np.uint64(32) 
                
                # mul_result[i+j - len(new_sum)] = mul_result[i+j - len(new_sum)] + new_sum[i+j - len(new_sum)]
                # carry = 1 if mul_result[i+j - len(new_sum)] < min(mul_result[i+j - len(new_sum)], new_sum[i+j - len(new_sum)]) else 0
                # mul_result[1+i+j - len(new_sum)] = carry + mul_result[1+ i+j - len(new_sum)] + new_sum[1 + i+j - len(new_sum)]
                hi_x = np.bitwise_and(x[i], mask_up) >> np.uint(32)
                hi_y = np.bitwise_and(y[j], mask_up) >> np.uint(32)
                lo_x = np.bitwise_and(x[i], mask_down)
                lo_y = np.bitwise_and(y[j], mask_down)

                print(hi_x, hi_y, lo_x, lo_y)

                new_sum[i+j+ 1], carry  = self.sum_3bit(lo_x*lo_y, (lo_x * hi_y) << np.uint64(32),(lo_y * hi_x) << np.uint64(32))
                new_sum[i+j], carry = self.sum_3bit(hi_x*hi_y,(lo_x * hi_y) >> np.uint64(32),(lo_y * hi_x) >> np.uint64(32), carry )

                mul_result[i+j +1], carry =  self.sum_3bit(a = mul_result[i+j +1], b = new_sum[i+j +1], carry = carry)
                mul_result[i+j], carry =  self.sum_3bit(a = mul_result[i+j ], b = new_sum[i+j], carry = carry)





        return mul_result
    
    def sum_3bit(self, a = 0 ,b = 0 , d = 0, carry = 0):
        temp = a + b
        carry = 1 if temp < min(a, b) else 0
        temp2 = temp + carry + d
        carry = 1 if temp2 < min(d, temp2) else 0
        return temp2, carry
    


    def __mul__(self, x):
        return self.long_mul(self.values, self.values.size, x.values, x.values.size)


np.seterr(over='ignore')
a = BigInt(2**50 + 2**76)
print(a)
b = BigInt(2**21 + 2**12)
c = a*b
d = BigInt((2**50 + 2**76 )*(2**21 + 2**12))
print(c)
print(d)

# mask_down = np.uint64(0x0000FFFF)
# mask_up = np.uint64(0xFFFF0000)
# a = np.uint64(1)
# b = np.uint64(2**17)
# print(b)
# print(np.bitwise_and(a, mask_down))
# print(np.bitwise_and(b, mask_up))