class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        a = int(str(dividend/divisor).split('.')[0])
        return a if (-2) ** 31 <= a <= 2 ** 31 - 1 else 2 ** 31 - 1


if __name__ == "__main__":
    print(Solution().divide(7,-3))
