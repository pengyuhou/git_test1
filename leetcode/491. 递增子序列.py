class Solution(object):
    def findSubsequences(self, nums):
        nums = list(enumerate(nums))
        ret = []
        def dfs(p, res):
            for i in range(len(p)):
                if not res:
                    res.append(p[i])
                    dfs(p, res)
                    res.pop()
                else:
                    if p[i][0] > res[-1][0] and p[i][1] >= res[-1][1]:
                        res.append(p[i])
                        dfs(p, res)
                        res.pop()
            if len(res) > 1 and (x := [i[1] for i in res.copy()]) not in ret:
                ret.append(x)
        dfs(nums, [])
        return ret


if __name__ == "__main__":
    print(Solution().findSubsequences([4, 6, 7, 7]))
