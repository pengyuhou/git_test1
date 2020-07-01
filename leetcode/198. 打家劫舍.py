"""
递归解法
"""


class Solution1(object):
    def rob(self, nums):
        if not nums:
            return 0
        l = len(nums)
        if l == 1:
            return nums[0]
        elif l == 2:
            return max(nums[:2])
        else:
            return max(self.rob(nums[:l-2])+nums[l-1], self.rob(nums[:l-1]))


"""
动态规划
"""


class Solution(object):
    def rob(self, nums):
        l = len(nums)

        if l == 0:
            return 0
        elif l == 1:
            return nums[0]
        elif l == 2:
            return max(nums)
        else:
            index = 2
            ret = [nums[0], max(nums[:2])]
            while index <= l-1:
                ret.append(max(ret[index-2]+nums[index], ret[index-1]))
                index += 1
            return ret[-1]


if __name__ == "__main__":
    nums = [183, 219, 57, 193, 94, 233, 202, 154, 65, 240, 97, 234, 100, 249, 186, 66, 90, 238,
            168, 128, 177, 235, 50, 81, 185, 165, 217, 207, 88, 80, 112, 78, 135, 62, 228, 247, 211]
    nums = [2, 7, 9, 3, 1]

    # nums=[]
    # nums= [1,2,3]
    # print(len(nums))
    print(Solution().rob(nums))
