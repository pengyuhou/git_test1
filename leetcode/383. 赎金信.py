class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        magazine = list(magazine)
        try:
            for i in ransomNote:
                a = magazine.index(i)
                magazine.pop(a)
            return True
        except:
            return False


print(Solution().canConstruct('aa','aba'))
