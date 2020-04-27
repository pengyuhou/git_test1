haystack = "hello"
needle = ""

class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        if needle=='':
            return 0
        a=haystack.split(needle)
        if len(a[0])==len(haystack):
            return -1

        return len(a[0])
s=Solution()
print(s.strStr(haystack, needle))



