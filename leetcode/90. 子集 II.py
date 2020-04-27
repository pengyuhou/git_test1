class Solution(object):
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        ret = []
        l = len(nums)
        count = {i: nums.count(i) for i in set(nums)}

        def dfs(p, res, level):
            if level == l + 1:
                return
            if res not in ret:
                ret.append(res.copy())

            for i in range(l):
                if not res:
                    res.append(p[i])
                    count[p[i]] -= 1
                    dfs(p, res, level + 1)
                    count[p[i]] += 1
                    res.pop()
                    continue
                if res and p[i] >= res[-1] and count[p[i]]:
                    res.append(p[i])
                    count[p[i]] -= 1
                    dfs(p, res, level + 1)
                    count[p[i]] += 1
                    res.pop()

        dfs(nums, [], 0)
        return ret


if __name__ == "__main__":
    nums = [1, 2, 2]
    print(Solution().subsetsWithDup(nums))
