# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

class Solution:
    def firstBadVersion(self, n):
        left = 1
        right = n
        while right-left>1:
            mid = (left + right) // 2
            if isBadVersion(mid):
                right = mid
            else:
                left = mid
        if isBadVersion(left):
            return left
        else:
            return right

