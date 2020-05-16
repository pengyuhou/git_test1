class Solution(object):
    def numberOfSubarrays(self, nums, k):
        a = {0: 1}
        odd = 0
        count = 0
        for i in range(len(nums)):
            if nums[i] % 2:
                odd += 1
            if odd - k in a.keys():
                count += a[odd - k]
            if odd in a.keys():
                a[odd] += 1
            else:
                a[odd] = 1
        return count


if __name__ == "__main__":
    print(Solution().numberOfSubarrays(nums=[1, 1, 2, 1, 1,1,1,1,4,5,2,61,4,1,], k=3))
