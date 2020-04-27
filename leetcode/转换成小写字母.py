class Solution(object):
    def toLowerCase(self, str):
        """
        :type str: str
        :rtype: str
        """
        s=str
        c = ''
        for i in range(len(s)):
            if s[i].isupper():
                c += s[i].lower()
            else:
                c += s[i]
        return c


if __name__ == '__main__':
    s="Hello"


    print(c)


