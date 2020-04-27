class Solution(object):
    def __init__(self):
        a = input()
        arr = a.split()
        self.arr = [int(i) for i in arr]
        self.num = self.arr[0]*self.arr[1]*self.arr[2]


    def fun(self):
        for i in range(1,self.num+1):
            if not i%self.arr[0] and not i%self.arr[1] and not i%self.arr[2]:
                return i


print(Solution().fun())







