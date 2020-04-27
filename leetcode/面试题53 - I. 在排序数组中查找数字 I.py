class Solution(object):
    def search(self, nums, target):
        if nums==[]:
            return 0
        l = len(nums)
        index1 = 0
        index2 = l-1
        flag = None
        if nums[index1]==target:
            flag=index1
        if nums[index2]==target:
            flag=index2
        while index1<index2:
            mid = (index1+index2)//2
            if nums[mid]>target:
                index2 = mid
            elif nums[mid]<target:
                index1 =mid
            else:
                flag = mid
                break
            if index2-index1==1:
                break
        count =0
        if flag!=None:
            for i in range(flag,l):
                if nums[i]==target:
                    count += 1
                else:
                    break
            for i in range(flag-1,-1,-1):
                if nums[i]==target:
                    count += 1
                else:
                    break
            return count
        else:
            return 0


if __name__ == "__main__":
    nums = [1,1]
    target =1
    print(Solution().search(nums,target))