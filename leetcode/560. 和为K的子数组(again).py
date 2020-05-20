class Solution(object):
    def subarraySum(self, nums, k):
        count = 0
        from collections import defaultdict
        a = defaultdict(int)
        a[0] = 1
        ret = 0
        for i in range(len(nums)):
            count += nums[i]
            if count - k in  a.keys():
                ret += a[count-k]
            a[count] += 1
        return ret



if __name__ == "__main__":
    print(Solution().subarraySum(nums=[1, 14, 1], k=2))
