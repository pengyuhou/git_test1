class Solution(object):
    def twoSum(self, nums, target):
        a=[num for num in nums if num<target]
        l=len(a)
        rear=l-1
        for i in range(l):
            while a[i]+a[rear]>target:
                rear-=1
            if a[i]+a[rear]==target:
                return [a[i],a[rear]]





if __name__ == "__main__":
    print(Solution().twoSum(nums,target))









