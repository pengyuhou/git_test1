class Solution(object):
    def search(self, nums, target):
        if nums==[]:
            return -1
        l = len(nums)
        if l==1:
            return 0 if target==nums[0] else -1

        index1 = 0
        index2 = l-1
        if nums[index1]==target:
            return index1
        if nums[index2]==target:
            return index2
        if l==2:
            return -1
        while index1 < index2:
            mid = (index1+index2)//2
            if nums[mid]==target:
                return mid
            if nums[mid]<target:
                index1 =mid
            if nums[mid]>target:
                index2 = mid
            if index2 - index1==1 and nums[index1]!=target and nums[index2]!=target:
                return -1





if __name__ == "__main__":
    nums = [-1, 0, 3, 5, 9, 12]
    nums = [2,5]
    print(Solution().search(nums,0))
