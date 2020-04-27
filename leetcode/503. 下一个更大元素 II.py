class Solution(object):
    def nextGreaterElements(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        db_nums = nums + nums
        l = len(nums)
        ret = []
        for i in range(len(nums)):
            index = i + 1
            key = nums[i]
            flag = False
            while index < l + i:
                if db_nums[index] > key:
                    flag =True
                    ret.append(db_nums[index])
                    break
                index += 1
            if not flag:
                ret.append(-1)
        return ret

if __name__ == "__main__":
    print(Solution().nextGreaterElements([]))
