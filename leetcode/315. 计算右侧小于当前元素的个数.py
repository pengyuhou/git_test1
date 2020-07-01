class Solution(object):
    def countSmaller(self, nums):
        import bisect
        ret = []
        res = []
        for num in reversed(nums):
            pos = bisect.bisect_left(ret, num)
            res.append(pos)
            ret.insert(pos, num)
        return res[::-1]

print(Solution().countSmaller([-1, -1]))








