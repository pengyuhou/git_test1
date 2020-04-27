class Solution(object):
    def lengthOfLastWord(self, s):
        ret = s.split(' ')
        l=len(ret)
        for i in range(l-1,-1,-1):
            if ret[i]!='':
                return len(ret[i])
        return 0


if __name__ == "__main__":
    s = "Hello World"
    # s="a    "
    s=''
    print(Solution().lengthOfLastWord(s))




