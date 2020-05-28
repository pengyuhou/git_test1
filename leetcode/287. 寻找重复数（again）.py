class Solution(object):
    def findDuplicate(self, nums):
        from collections import defaultdict
        d = defaultdict(int)
        for num in nums:
            d[num] += 1
            if d[num] > 1:
                return num


if __name__ == "__main__":
    print(Solution().findDuplicate([1, 3, 4, 2, 2]))
