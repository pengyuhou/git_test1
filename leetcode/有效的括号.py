s="{()}"

class Solution():
    def isValid(self, s):
        while '()' in s or '[]' in s or '{}' in s:
            s=s.replace('()','')
            s=s.replace('{}','')
            s=s.replace('[]','')
        return s == ''

uu=Solution()
print(uu.isValid(s))










