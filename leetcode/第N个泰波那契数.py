class Solution(object):
    def tribonacci(self, n):
        a=0
        b=1
        c=1
        list1=[]
        n += 1
        for i in range(n):
            d = a+b+c
            list1.append(a)
            a = b
            b = c
            c = d
        return list1[len(list1)-1]
s=Solution()
print(s.tribonacci(4))








