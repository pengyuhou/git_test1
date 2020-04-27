class Solution(object):
    def rotate(self, nums, k):
        a=nums.copy()
        index=0
        for i in range(len(nums)):
            if i<k:
                nums[i]=a[len(nums)-k+i]
            else:
                nums[i]=a[index]
                index += 1

if __name__ == "__main__":
    nums=[-1]
    k=2
    print(Solution().rotate(nums,k))
    print(nums)







