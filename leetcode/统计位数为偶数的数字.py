class Solution(object):
    def findNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        index = 0
        for num in nums:
            if not len(str(num)) % 2:
                index += 1
        return index

if __name__ == "__main__":
    nums = [12, 345, 2, 6, 7896]





