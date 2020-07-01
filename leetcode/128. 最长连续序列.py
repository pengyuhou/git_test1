class Solution(object):
    def longestConsecutive(self, nums):
        nums = set(nums)
        l = len(nums)
        if l == 1:
            return 1
        res = sorted(nums)
        cnt = 1
        ret = -float('inf')
        for i in range(1, l):
            if res[i] - res[i - 1] == 1:
                cnt += 1
            else:
                cnt = 1
            ret = max(ret, cnt)
        return ret if ret != -float('inf') else 0


print(Solution().longestConsecutive([0, 1, 2, 0, 2, 3]))
