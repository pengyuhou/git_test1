strs=["dog","racecar","car"]
# "fl"


b=["flower","flow","flight"]



a=["aa","a"]





class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        x=''
        if strs!=[]:
            t=len(strs[0])
            for i in range(t):
                k=strs[0][i]
                for str in strs:
                    if   i>=len(str) or k!=str[i] :
                        return x
                x += k
            return x
        else:
            return ''


# class Solution:
#     def longestCommonPrefix(self, strs) :
#         x = ''
#         if strs:
#             for i in range(len(strs[0])):
#                 k = strs[0][i]
#                 for s in strs:
#                     if i>=len(s) or s[i]!=k:
#                         return x
#                 x+=k
#         return x


s=Solution()
print(s.longestCommonPrefix(a))











