from functools import reduce
import math

a = [1, 2, 3, 4, 5, 6, 7, 8]
res = map(lambda x: x ** 2, a)
ret = filter(lambda x: x > 100, a)
ret2 = reduce(lambda x, y: x * y, a)
print(ret2)

a = 0x13
print(hex(a))

print('5' * 7)

a = []
print(isinstance(a, tuple))

a = [1, 31, 4, 13, 54, 56, 3, 6, 437]


def fun(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        index = i - 1
        while index >= 0 and key < arr[index]:
            arr[index], arr[index + 1] = arr[index + 1], arr[index]
            index -= 1
    return arr


print(fun(a))
