class Solution1(object):
    def fib(self, N):
        """
        :type N: int
        :rtype: int
        """
        if N==0:
            return 0
        if N==1 or N==2:
            return 1
        else:
            return self.fib(N-1)+self.fib(N-2)


class Solution(object):
    def fib(self, N):
        a=1
        b=1
        if N==0:
            return 0
        while N-1:
            c=a+b
            a=b
            b=c
            N -= 1
        return a




if __name__ == "__main__":
    S=Solution()
    print(S.fib(4))


