class Solution(object):
    def minSubArrayLen(self, s, nums):
        index1 = 0
        index2 = 0
        ret = float('inf')
        while index1 <= index2 and index2 < len(nums) + 1:
            if sum(nums[index1:index2]) < s:
                index2 += 1
            else:
                ret = min(ret, len(nums[index1:index2]))
                index1 += 1
        return ret if ret != float('inf') else 0


if __name__ == "__main__":
    print(Solution().minSubArrayLen(
        100, []
    ))
