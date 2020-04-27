class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        t1 = t
        for i in s:
            if i in t:
                t1 = t1.replace(i, '', 1)
        for j in list(t1):
            if j in t:
                t = t.replace(j, '', 1)
        if t==s:
            return True
        else:
            return False

if __name__ == '__main__':
    s="acb"
    t="ahbgdc"









    S=Solution()
    print(S.isSubsequence(s,t))






