class Solution(object):
    def numberOfSubarrays(self, nums, k):
        from collections import defaultdict
        d = defaultdict(int)
        d[0] = 1
        count = 0
        ret = 0
        for num in nums:
            if num % 2:
                count += 1
            if count-k in d.keys():
                ret += d[count-k]
            d[count] += 1
        return ret



if __name__ == "__main__":
    print(Solution().numberOfSubarrays(nums=[1, 1, 2, 1, 1], k=3))
