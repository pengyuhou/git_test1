class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        ret = []
        l = len(nums)

        def dfs(p, res, level):
            if level == l + 1:
                return
            if res not in ret:
                ret.append(res.copy())

            for i in range(l):
                if not res:
                    res.append(p[i])
                    dfs(p, res, level + 1)
                    res.pop()
                    continue
                if res and p[i]>res[-1]:
                    res.append(p[i])
                    dfs(p, res, level + 1)
                    res.pop()

        dfs(nums, [], 0)
        return ret


if __name__ == "__main__":
    nums = [1, 2, 3]
    print(Solution().subsets(nums))
