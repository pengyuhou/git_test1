class Solution(object):
    def majorityElement(self, nums):
        l = len(nums)
        if l==1:
            return nums[0]
        a={}
        for i in nums:
            if i not in a.keys():
                a[i]=1
            else:
                a[i] += 1
                if a[i]>l//2:
                    return i



if __name__ == "__main__":
    nums = [1]
    print(Solution().majorityElement(nums))





