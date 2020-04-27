class Solution(object):
    def findUnsortedSubarray(self, nums):
        nums_sort = sorted(nums)
        l = len(nums)
        index1 = 0
        ret=[]
        while index1<l:
            if nums_sort[index1] != nums[index1]:
                ret.append(index1)
            index1 += 1
        if ret:
            return ret[-1]-ret[0]+1
        else:
            return 0






if __name__ == "__main__":
    nums = [5,4,3,2,1]
    nums=[1,2,3,4]
    # nums = [3,2,3,2,4]
    # nums = [1, 3, 2, 3, 3]


    # nums = [2, 6, 4, 8, 10, 9,15]
    # nums = [2,3,3,2,4]
    print(Solution().findUnsortedSubarray(nums))












