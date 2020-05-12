import os
import sys
import math
from functools import reduce
import random
import datetime
import time
import calendar
import hashlib
import hmac

# 获取操作系统的名字
# print(os.name)
# print(os.sep)
# print(os.environ)


# print(math.factorial(10))
# a = range(1, 11)
# print(reduce(lambda x, y: x * y, a))

res = random.sample(['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h'], 1)
print(random.choice(res))
print(res)

print(datetime.datetime.now())
print(time.time())
print(time.ctime())
print(time.asctime())

print(calendar.calendar(15645615))

x = hashlib.md5()
x.update('abc'.encode('utf-8'))
print(x.hexdigest())


class ppl:
    def __init__(self, name, age, money):
        self.name = name
        self.age = age
        self.__money = money


a = ppl('张三', '男', 10000)
print(a.name)
print(a.age)
print(a._ppl__money)

