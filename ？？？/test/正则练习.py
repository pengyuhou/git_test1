import re

# import datetime
#
# print(datetime.datetime.now())
#
# print(divmod(10, 5))
#
# res = [i * 11 for i in range(1, 10)]
# print(res)
#
# a = [1, 2, 3, 4, 5, 1]
# b = [1, 2, 10]
# print(a)
# print(set(a) & set(b))
#
# a.extend(b)
# print(a)


a = {1: 'asd', 2: 'adsa', 3: '1q', 5: 'asdas', 4: 'ada'}
res = sorted(a.items(), key=lambda x: x[0])

res = sorted(a.keys())
ret = {i: a[i] for i in res}
print(ret)

print(float())

# res = sorted(a)
#
# ret = {i: a[i] for i in res}
# print(ret)
#
# a = [[1, 2], [3, 4], [5, 6]]
# print(a)
# res = [j for i in a for j in i]
# print(res)
# a = '1'
# a = '    123123     '
# print(a)
# print(a.lstrip())

s = '786490473@qq.com'
import re
regx = re.compile('[0-9]+@qq.com')
print(*regx.findall(s))



s = 'afrfb'
x = re.compile('[abc]')
print(x.findall(s))











