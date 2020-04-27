class Solution(object):
    def isRectangleOverlap(self, rec1, rec2):
        """
        :type rec1: List[int]
        :type rec2: List[int]
        :rtype: bool
        """
        if (rec2[0]<rec1[2] and rec2[1]<rec1[3] ) and (rec2[2]>rec1[0] and rec2[3]>rec1[1]):
            return True
        else:
            return False

if __name__ == "__main__":
    rec1 = [0, 0, 1, 1]
    rec2 = [1, 0, 2, 1]
    rec1 = [5,15,8,18]
    rec2 = [0,3,7,9]
    print(Solution().isRectangleOverlap(rec1,rec2))