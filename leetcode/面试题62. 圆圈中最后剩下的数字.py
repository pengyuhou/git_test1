class Solution:
    def lastRemaining(self, n: int, m: int) -> int:
        ret = list(range(n))
        index = 0
        for _ in range(n-1):
            index += m-1
            index = index%len(ret)
            ret.pop(index)
        return ret[0]



if __name__ == "__main__":
    n = 10
    m = 17
    print(Solution().lastRemaining(n,m))




