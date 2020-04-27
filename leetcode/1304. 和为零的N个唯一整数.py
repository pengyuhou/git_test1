class Solution(object):
    def sumZero(self, n):
        ret = []
        if n % 2:
            for i in range(1, n // 2 + 1):
                ret.append(i)
                ret.append(-i)
            ret.append(0)
        else:
            for i in range(1, n // 2 + 1):
                ret.append(i)
                ret.append(-i)
        return ret


if __name__ == "__main__":
    n = 6
    print(Solution().sumZero(n))




