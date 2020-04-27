class Solution(object):
    def arrayPairSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums = sorted(nums)
        ret = []
        for i in range(len(nums)):
            if not i % 2:
                ret.append(nums[i])
        return sum(ret)
if __name__ == '__main__':
    nums=[1,4,3,2]
    nums=sorted(nums)
    ret=[]
    for i in range(len(nums)):
        if not i%2:
            ret.append(nums[i])
    print(sum(ret))

