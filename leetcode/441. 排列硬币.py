class Solution:
    def arrangeCoins(self, n: int) -> int:
        cur = 1
        count = 0
        while True:
            count += cur
            if count > n:
                return cur-1
            cur += 1

if __name__ == "__main__":
    n = 0
    print(Solution().arrangeCoins(n))





