class Solution:
    def validMountainArray(self, A):
        nums=A
        index=0
        l=len(nums)
        if l==1 or l==0:
            return False
        flag=False
        while nums[index]<nums[index+1]:
            index += 1
            if index +1>l-1:
                return False
            flag=True
        if flag:
            while nums[index]>nums[index+1]:
                index += 1
                if index+1>l-1:
                    return True
        return False

if __name__ == "__main__":
    nums=[]
    print(Solution().validMountainArray(nums))







