class Solution(object):
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        l = len(nums)
        pd = [False for _ in range(l)]
        ret = []
        def dfs(p, pd, level, res):
            if level == l + 1:
                if res.copy() not in ret:
                    ret.append(res.copy())
                return
            for i in range(l):
                if not pd[i]:
                    pd[i] = True
                    res.append(p[i])
                    dfs(p,pd,level+1,res)
                    pd[i] = False
                    res.pop()
        dfs(nums,pd,1,[])
        return ret


if __name__ == "__main__":
    print(Solution().permuteUnique([1, 1, 2]))
