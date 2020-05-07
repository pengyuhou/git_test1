class Solution:
    def lastRemaining(self, n: int, m: int) -> int:
        res = list(range(n))
        index = 0
        while len(res) != 1:
            index += m-1
            if index>=len(res):
                index = index%len(res)
            res.pop(index)
        return res[0]


if __name__ == "__main__":
    n = 10
    m = 17
    print(Solution().lastRemaining(10,17))
