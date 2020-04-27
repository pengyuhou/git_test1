class Solution(object):
    def maxSubArray(self, nums):
        index,l = 0 ,len(nums)
        if nums == []:
            return 0
        ret = []
        while index<l:
            if index==0:
                sum_total=nums[index]
                max_val = sum_total
                ret.append(max_val)
                index += 1
                continue
            if nums[index]>=nums[index]+sum_total:
                sum_total = nums[index]
                max_val = sum_total
                ret.append(max_val)
                index += 1
                continue
            else:
                sum_total += nums[index]
                index += 1
                if sum_total>max_val:
                    max_val = sum_total
                    ret.append(max_val)
        return max(ret)





if __name__ == "__main__":
    print(Solution().maxSubArray( [-1,-2]))


