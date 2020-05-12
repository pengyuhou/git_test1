import time


def fun2(func):
    def inner(*args):
        a = time.time()
        x = func(args[1])
        print(time.time() - a)
        return x

    return inner


@fun2
def fun1(x):
    count = 0
    for i in range(1, x):
        count += i
    return count


print(fun1(10, 6))


class Studnet:
    name = None

    def fun1(self, name):
        self.name = name


def fun():
    for i in range(1, 10):
        yield i


a = [1, 2, 3, 4]
b = [4, 5, 6]
res = map(lambda x, y: x + y, a, b)
print(list(res))

from functools import reduce

def fun(x,y):
    return x*y


res = reduce(fun, a)
print(res)

a = '12345'















