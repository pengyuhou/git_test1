# class insertion_sort():
#     # 插入排序算法 最好O（n） 最坏O（n**2）
#     def fun(self, a):
#         for i in range(1, len(a)):
#             key = a[i]
#             j = i - 1
#             while j >= 0 and a[j] > key:
#                 a[j + 1] = a[j]
#                 j -= 1
#             a[j + 1] = key
#         return a


a = [3, 2, 388, 67, 4, 5, 8, 9, 3, 4, 5]

for i in range(1, len(a)):
    key = a[i]
    j = i - 1
    while j >= 0 and a[j] > key:
        a[j+1] = a[j]
        j -= 1
    a[j+1] = key
print(a)








