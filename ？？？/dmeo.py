# import math
#
# x = ((50 ** 2 + 110 ** 2 - 2 * 50 * 110 * math.cos(math.pi / 6)) ** 0.5)
#
# # print(math.sin(math.pi/6))
# print(x * math.sin(2 * math.pi * 70 / 360) / math.sin(2 * math.pi * 40 / 360))
# print(110 * 0.5 / 71.23)
#
# print(all([True, True, False]))
#
# a = '   afasdfa   afdasd   '
# ret = a.split()
# print(ret)
#
# a = 10
# x = '13123123'
# print(int(a))
#
# a = [1, 3, 4, 5, 6, 72, 4]
# print(sorted(a))
#
# a = lambda x, y: x + y
#
# res = [a]
#
# print(res[0](6,7))

# from functools import reduce
#
# a = [1, 2, 3]
# res = reduce(lambda x, y: x * y, a)
# print(res)
#
# from collections import defaultdict
#
# d = defaultdict(int)
#
# a = ['a', 'b', 'a']
# for i in a:
#     d[i] += 1
# print(d)

# a = 'asdas'
# def fun():
#     print(a)
# print(fun())

from collections import *

C = Counter()
a = ['a', 'b', 'a', 'v', 'a']
ret = [C.copy()]
for i in a:
    C[i] += 1
    ret.append(C.copy())

for i in range(1, len(ret)):
    print(ret[i] - ret[i - 1])


