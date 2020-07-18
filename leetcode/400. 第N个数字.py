class Solution:
    def findNthDigit(self, n: int) -> int:
        index = 1
        while True:
            n -= (9 * 10 ** (index - 1)) * index
            if n <= 0:
                break
            index += 1
        digit = index
        idx = n % digit
        if idx == 0:
            idx = digit
        n += (9 * 10 ** (index - 1)) * index
        number = 10 ** (digit - 1) + n // digit if idx != digit else 10 ** (digit - 1) + n // digit - 1

        for i in range(idx, digit):
            number //= 10
        return number % 10



if __name__ == "__main__":
    print(Solution().findNthDigit(10))
