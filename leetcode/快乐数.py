class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        pre=[]
        while True:
            n_pre = n
            sum = 0
            for i in str(n):
                a = int(i) * int(i)
                sum += a
            n = sum
            pre.append(n)

            if n == 1:
                return True
            if len(pre) != len(set(pre)):
                return False


if __name__ == '__main__':
    s=Solution()
    print(s.isHappy(19))










