class Solution(object):
    def numberOfArithmeticSlices(self, A):
        dp = [[False for _ in range(len(A))] for _ in range(len(A))]
        for j in range(2, len(A)):
            for i in range(j - 2, -1, -1):
                if j - i == 2:
                    if A[j] - A[i] == 2 * (A[j] - A[i + 1]):
                        dp[i][j] = True
                if dp[i][j - 1] and A[j] - A[j - 1] == A[j - 1] - A[j - 2]:
                    dp[i][j] = True
        return sum([i.count(True) for i in dp])


def issushu(n):
    for i in range(2, int(n ** 0.5) + 1):
        if not n % i:
            return False
    return True


if __name__ == '__main__':
    print(Solution().numberOfArithmeticSlices([7, 7, 7, 7]))
    print(issushu(6))
