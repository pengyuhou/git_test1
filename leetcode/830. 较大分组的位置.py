class Solution(object):
    def largeGroupPositions(self, S):
        """
        :type S: str
        :rtype: List[List[int]]
        """
        s = list(S)
        l = len(s)
        index = 0
        ret = []
        while index<l:
            tmp = index
            count = 1
            while index+1<l and s[index]==s[index+1]:
                count += 1
                index += 1
            if count>2:
                ret.append([tmp,index])
            index += 1
        return ret

if __name__ == "__main__":
    s = "abcdddeeeeaabbbcd"
    print(Solution().largeGroupPositions(s))

