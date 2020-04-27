class Solution(object):
    def maxSlidingWindow(self, nums, k):
        if nums==[]:
            return []
        l = len(nums)
        ret = []
        for i in range(l - k + 1):
            ret.append(max(nums[i:i + k]))
        return ret

if __name__ == "__main__":
    nums = [1, 3, -1, -3, 5, 3, 6, 7]
    k = 3
    nums = [1,2]
    k=1
    print(Solution().maxSlidingWindow(nums,k))





