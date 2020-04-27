class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        l = len(nums)
        ret = []
        pd = [False for _ in range(l)]
        def dfs(p,pd,level,res):
            if level==l+1:
                ret.append(res.copy())
                return
            for i in range(l):
                if not pd[i]:
                    pd[i] = True
                    res.append(nums[i])
                    dfs(p,pd,level+1,res)
                    pd[i] = False
                    res.pop()
        dfs(nums,pd,1,[])
        return ret