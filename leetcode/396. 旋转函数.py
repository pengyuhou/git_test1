class Solution(object):
    def maxRotateFunction(self, A):
        ret, l = [sum(map(lambda x, y: x * y, range(len(A)), A))], len(A)
        s = sum(A)
        for i in range(1, l):
            ret.append(ret[-1] + s - l * A[l - i])
        return max(ret) if ret else 0


if __name__ == '__main__':
    print(Solution().maxRotateFunction([4, 3, 2, 6]))

