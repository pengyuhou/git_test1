class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        a = nums.copy()
        nums.sort()
        mark = [False] * len(nums)
        ret = []
        l = len(nums)
        def dfs(p, pd, level, res):
            if level == l + 1:
                if res not in ret:
                    ret.append(res.copy())
                return
            for i in range(l):
                if not pd[i]:
                    pd[i] = True
                    res.append(p[i])
                    dfs(p,pd,level+1,res)
                    res.pop()
                    pd[i] = False
        dfs(nums,mark,1,[])
        nums[:] = ret[ret.index(a)+1] if ret.index(a)+1<len(ret) else ret[0]


if __name__ == "__main__":
    print(Solution().nextPermutation([2,2,7,5,4,3,2,2]))
