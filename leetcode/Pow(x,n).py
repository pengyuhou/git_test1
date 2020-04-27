class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        return float(format(pow(x,n),'.5f'))


class Solution1(object):
    def myPow(self, x, n):
        num=1
        if n<0:
            for i in range(abs(n)):
                num *= x
            num = 1/num
        for i in range(n):
            num *= x



        return num

s=Solution1()
print((s.myPow(2.00000, 1)))





