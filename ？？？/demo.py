# # import tensorflow
# #
# # import torch
#
#
# # # print(tensorflow.abs(-5))
# # class a:
# #     pass
# # xx = a()
# # print(isinstance(xx,a))
#
#
# # a = [12, 2]
# # b = [4, 5]
# # a += b
# # a = {'name': 'hpy', 'age': 18}
# #
# # print([(i, a[i]) for i in a])
#
# # s = '2020-09-20 adasda 2018-11-11 ga哈哈'
# # import re
# #
# # res = re.sub("(\d{4})-(\d{2})-(\d{2})", "\\2/\\3/\\1", s)
# # print(res)
#
#
# # a = [[1, 2, 3], [3, 4], [5, 6]]
# # print(a)
# import re
# # 使用re split 拆分字符串
# # s = 'asd\qafdaf|adsfa?sdf2  qeb&ndb*    fsgbm#rmfga'
# # print(s.encode('utf-8'))
# # print(re.split('[\*|?&#\t ]+', s))
#
# # def fun():
# #     for i in range(10):
# #         yield i
# # for i in fun():
# #     print(i)
#
# from collections import Iterable, Iterator
#
# l = [1, 2, 3, 4, 5, 6]
# it = iter(l)
# print(isinstance(it,Iterable))
# # for i in it:
# #     print(i)
#
# # for i in iter(l):
# #     print(i)
#
# # print(iter(l))
# # print(l.__iter__())


# a = [1,2,3,4]
# b = ['asda','ads']
# print([*a,*b])
#
#

# for i in iter(int, 1):
#     print('--')


# a = 'qwer'
# print(''.join(list(reversed(a))))
# print("aabb".count(''))
#
# print('m'.count(''))


# ***********   找到缺失的数字程序    ************************
def find_Lost_Nums(nums):
    nums.sort()
    cur = 1
    ret = []
    for i in nums:
        if i ^ cur != 0:
            ret.append(cur)
            cur += 1
        if len(ret) == 2:
            break
        cur += 1
    return ret


# print(fun([7, 5, 4, 3, 1]))


print(10 ^ 0)
