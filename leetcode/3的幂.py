class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        for i in range(l:=10):
            print(l)
        if n <= 0:
            return False
        while n > 1:
            res = n % 3
            if res:
                return False
            n = n // 3
        return True



if __name__ == "__main__":
    n = -3
    print(Solution().isPowerOfThree(n))
