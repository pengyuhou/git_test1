import math


class Solution:
    def trailingZeroes(self, n: int) -> int:
        count = 0
        while n:
            if n < 5:
                break
            count += n//5
            n //= 5
        return count


if __name__ == "__main__":
    n = 120
    print(Solution().trailingZeroes(n))
