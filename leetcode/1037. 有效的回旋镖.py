class Solution:
    def isBoomerang(self, points):
        nums=points
        if nums[0] != nums[1] and nums[0] != nums[2] and nums[1] != nums[2]:
            if (nums[0][1] - nums[1][1]) != 0 and (nums[0][1] - nums[2][1])!=0:
                if (nums[0][0] - nums[1][0]) / (nums[0][1] - nums[1][1]) == (nums[0][0] - nums[2][0]) /(nums[0][1] - nums[2][1]):
                    return False
                else:
                    return True
            elif (nums[0][1] - nums[1][1]) == 0 and (nums[0][1] - nums[2][1])==0:
                return False
            else:
                return True
        else:
            return False


if __name__ == "__main__":
    li=[[1,1],[2,2],[3,3]]
    print(Solution().isBoomerang(li))










