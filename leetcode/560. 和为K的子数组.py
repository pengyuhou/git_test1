class Solution(object):
    def subarraySum(self, nums, k):
        a = {0: 1}
        cur_sum = 0
        count = 0
        for i in range(len(nums)):
            cur_sum += nums[i]
            if cur_sum - k in a.keys():
                count += a[cur_sum - k]
            if cur_sum in a.keys():
                a[cur_sum] += 1
            else:
                a[cur_sum] = 1
        return count


if __name__ == "__main__":
    print(Solution().subarraySum(nums=[1], k=0))
