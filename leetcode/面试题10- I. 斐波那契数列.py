class Solution(object):
    def fib(self, n):
        if n == 0:
            return 0
        if n == 1:
            return 1
        if n>1:
            a = 0
            b = 1
            while n-1:
                c = b
                b = a+b
                a = c
                n -= 1
            return  b%1000000007





if __name__ == "__main__":
    print(Solution().fib())

