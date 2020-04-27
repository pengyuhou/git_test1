class Solution(object):
    def waysToStep(self, n):
        if n==1:
            return 1
        if n==2:
            return 2
        if n==3:
            return 4
        if n>=4:
            a=1
            b=2
            c=4
            index = 3
            while index<n:
                tmp=c
                c=(a+b+c)%1000000007
                a=b
                b=tmp
                index += 1
            return c

if __name__ == "__main__":
    n=900750
    print(Solution().waysToStep(n))





