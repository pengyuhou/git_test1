class Solution:
    def lastRemaining(self, n: int, m: int) -> int:
        res = list(range(n))
        index = 0
        while len(res) != 1:
            index += m - 1
            if index >= len(res):
                index = index % len(res)
            res.pop(index)
        return res[0]


if __name__ == "__main__":
    n = 10
    m = 17
    print(Solution().lastRemaining(10, 17))

    a = [1, 2, 3, 4,[12312,123]]
    a = (tuple(a))
    print(a)
    a[4][1] = 'nihao'
    print(a)

