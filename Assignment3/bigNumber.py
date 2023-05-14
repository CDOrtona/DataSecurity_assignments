import numpy as np


# def from_num_to_array(number, value):
#     if type(number) ==bytes:
#         number = int.from_bytes(number,"big")
#     bit_num = bin(number)[2:]
#     bit_num = (value*64-len(bit_num))*'0' + bit_num

#     arr = [int(bit_num[i:i+64],2) for i in range(0, len(bit_num), 64)]

#     return np.array(arr)

def from_num_to_array(number, value=None):
    if isinstance(number, bytes):
        number = int.from_bytes(number, "big")

    print(number)
    print(bin(number))

    arr = np.array([(number >> ((value - i - 1) * 64)) & 0xFFFFFFFFFFFFFFFF for i in range(value)], dtype=np.uint64)

    return arr

print(from_num_to_array(2 ** 8, 8))


def big_sum(x, y):
    sum_result = np.zeros_like(x, dtype=np.uint64)
    carry = 0
    for i in range(len(x) - 1, -1, -1):
        temp_sum = int(x[i]) + int(y[i]) + carry
        sum_result[i] = temp_sum % 2 ** 64
        carry = temp_sum // 2 ** 64

    return sum_result


def big_mul(x, valuex, y, valuey):
    mul_result = np.zeros(valuex + valuey, dtype=np.uint64)
    for i in range(len(x) - 1, -1, -1):
        new_sum = np.zeros(valuex + valuey, dtype=np.uint64)
        for j in range(len(y) - 1, -1, -1):
            new_sum[len(new_sum) + i - len(x)] = int(x[i]) * int(y[j]) % 2 ** 64
            new_sum[len(new_sum) + i - len(x) - 1] = int(x[i]) * int(y[j]) // 2 ** 64
            mul_result = mul_result + new_sum

    return mul_result


print(big_mul(from_num_to_array(3, 3), 3, from_num_to_array(8, 3), 2))
