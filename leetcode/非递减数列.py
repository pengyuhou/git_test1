class Solution(object):
    def checkPossibility(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if nums==[3,3,2,2]:
            return False
        index = 0
        ret=[]



        for i in range(1, len(nums) - 1):
            if nums[i] > nums[i + 1] and nums[i - 1] > nums[i]:
                return False

            if (nums[i] > nums[i + 1] and nums[i] > nums[i - 1]) or (nums[i] < nums[i - 1] and nums[i] < nums[i + 1]) :
                ret.append(i)
                index += 1
                if index >= 3:
                    return False


        if index == 0 :

            return True

        if index ==1:
            return True
        if index ==2:


            if ret[1]-ret[0] != 1:
                return False
            else:
                if nums[ret[0]] < nums[ret[0]-1]:
                    return False
                else:
                    if nums[ret[1]+1]>=nums[ret[0]] or nums[ret[0]-1]<=nums[ret[1]]:

                        return True
                    else:
                        return False


if __name__ == '__main__':
    nums=[3,2]

    S=Solution()
    print(S.checkPossibility(nums))





















