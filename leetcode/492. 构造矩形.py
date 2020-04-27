class Solution(object):
    def constructRectangle(self, area):
        """
        :type area: int
        :rtype: List[int]
        """
        s=area
        a = int(s ** 0.5)
        ret = []
        for i in range(1, a + 1):
            if not s % i:
                ret.append([i, s // i])
        res = sorted(ret, key=lambda x: x[1] - x[0])
        res[0].reverse()
        return res[0]

if __name__ == "__main__":
    s = 4
    print(Solution().constructRectangle(25))


