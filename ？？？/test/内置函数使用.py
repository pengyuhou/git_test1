from functools import reduce
import math

a = [1, 2, 3, 4, 5, 6, 7, 8]
res = map(lambda x: x ** 2, a)
ret = filter(lambda x: x > 100, a)
ret2 = reduce(lambda x, y: x * y, a)
print(ret2)


