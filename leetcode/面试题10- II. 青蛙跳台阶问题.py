class Solution:
    def numWays(self, n: int) -> int:
        if n==0 or n==1:
            return 1
        if n==2:
            return 2
        if n>=3:
            a = 1
            b = 2
            index = 2
            while index<n:

                a,b = b,a+b
                index += 1
            return b%1000000007

if __name__ == "__main__":

    print(Solution().numWays(44))
