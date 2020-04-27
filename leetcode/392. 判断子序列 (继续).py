class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        print(t)
        t=iter(t)
        print(t)
        a = [i in t for i in s]
        return all(a)



if __name__ == "__main__":
    s = "abc"
    t = "ahbgdc"
    s = "axc"
    t = "ahbgdc"
    s="acb"
    t="ahbgdc"


    print(Solution().isSubsequence(s,t))










