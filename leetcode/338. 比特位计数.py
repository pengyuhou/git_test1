class Solution(object):
    def countBits(self, num):
        """
        :type num: int
        :rtype: List[int]
        """
        ret = []
        for i in range(num+1):
            ret.append(str(bin(i)).count('1'))
        return ret




if __name__ == "__main__":
    print(Solution().countBits(2))











