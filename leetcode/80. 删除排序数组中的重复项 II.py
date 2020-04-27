class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        a = list(sorted(set(nums)))
        res = []
        for i in a:
            if nums.count(i) > 2:
                res += [i] * 2
            else:
                res += [i] * nums.count(i)
        nums[:] = res
        return len(nums)


if __name__ == "__main__":
    print(Solution().removeDuplicates([-1,0,0,0,0,3,3]))
