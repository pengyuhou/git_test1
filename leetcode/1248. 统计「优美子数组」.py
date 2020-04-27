class Solution(object):
    def numberOfSubarrays(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        l = len(nums)
        ret = [-1]
        for i in range(l):
            if nums[i] % 2:
                ret.append(i)
        ret.append(l)
        count = 0

        for i in range(1, len(ret) - k):
            count += (ret[i] - ret[i - 1]) * (ret[i + k] - ret[i + k - 1])
        return count


if __name__ == "__main__":
    nums = [1,1,2,1,1]
    k = 3
    print(Solution().numberOfSubarrays(nums, k))
