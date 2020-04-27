class Solution(object):
    def summaryRanges(self, nums):
        res = []
        index = 0
        while index < len(nums):
            ret = []
            ret.append(str(nums[index]))
            index += 1
            while index < len(nums) and nums[index] == nums[index - 1] + 1:
                ret.append(str(nums[index]))
                index += 1
            if len(ret)>1:
                res.append('{}->{}'.format(ret[0],ret[-1]))
            else:
                res.append(ret[0])
        return res

if __name__ == "__main__":
    print(Solution().summaryRanges([]))
