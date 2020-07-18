# # # import math
# # #
# # # x = ((50 ** 2 + 110 ** 2 - 2 * 50 * 110 * math.cos(math.pi / 6)) ** 0.5)
# # #
# # # # print(math.sin(math.pi/6))
# # # print(x * math.sin(2 * math.pi * 70 / 360) / math.sin(2 * math.pi * 40 / 360))
# # # print(110 * 0.5 / 71.23)
# # #
# # # print(all([True, True, False]))
# # #
# # # a = '   afasdfa   afdasd   '
# # # ret = a.split()
# # # print(ret)
# # #
# # # a = 10
# # # x = '13123123'
# # # print(int(a))
# # #
# # # a = [1, 3, 4, 5, 6, 72, 4]
# # # print(sorted(a))
# # #
# # # a = lambda x, y: x + y
# # #
# # # res = [a]
# # #
# # # print(res[0](6,7))
# #
# # # from functools import reduce
# # #
# # # a = [1, 2, 3]
# # # res = reduce(lambda x, y: x * y, a)
# # # print(res)
# # #
# # # from collections import defaultdict
# # #
# # # d = defaultdict(int)
# # #
# # # a = ['a', 'b', 'a']
# # # for i in a:
# # #     d[i] += 1
# # # print(d)
# #
# # # a = 'asdas'
# # # def fun():
# # #     print(a)
# # # print(fun())
# #
# # from collections import *
# #
# # C = Counter()
# # a = ['a', 'b', 'a', 'v', 'a']
# # ret = [C.copy()]
# # for i in a:
# #     C[i] += 1
# #     ret.append(C.copy())
# #
# # for i in range(1, len(ret)):
# #     print(ret[i] - ret[i - 1])
# #
# #
#
# # a = filter(lambda x:x>0,[1,2,3,4])
# # print(next(a))
# # print(next(a))
# # a = {'name': 'hpy', 'age': 12}
# # print(a.items())
# #
# # from collections import namedtuple
# #
# # nt = namedtuple('student', ['name', 'age', 'id'])
# # a = nt('hpy', 20, 1806014413)
# # print(a.id)
# #
# # a = {'a': 61, 'b': 87, 'c': 94}
# #
# # print(dict(sorted(a.items(), key=lambda x: x[1], reverse=True)))
# # a = [1, 2, 2]
# # b = [10, 10, 10]
# # print(tuple(zip(a, b)))
# # s = set([12, 3])
# # s1 = set([12, 5])
# # print(s1 - s)
#
# d = {}
# d['a'] = 1
# d['b'] = 2
# d['c'] = 3
# print(d.keys())
#
# from collections import deque
#
# d = deque()
# d.append(10)
# d.append(2)
# d.popleft()
# print(d)
#
#

# import bisect
#
# a = [1, 2, 3, 3, 4]
# print(bisect.insort(a, 3))
# print(a)

#
# a = {'name': 'hpy', 'age': 18}
# b = {'id': 12312}
# res = {**a, **b}


a = [1, 3, 4]
import bisect

print(bisect.bisect_right(a, 3))
import numpy

a = numpy.array([1, 2, 3, 3, 4])

from PyQt5 import Qt as qt
qt.


