class Solution:
    def climbStairs(self, n: int) -> int:
        if n==1:
            return 1
        elif n==2:
            return 2
        elif n==3:
            return 3
        else:
            ret=[1,2,3]
            while n-4>=0:
                ret.append(ret[-1]+ret[-2])
                n -= 1
            return ret[-1]

if __name__ == "__main__":
    n = 5
    print(Solution().climbStairs(n))



