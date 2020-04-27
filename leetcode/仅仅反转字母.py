class Solution(object):
    def reverseOnlyLetters(self, S):
        """
        :type S: str
        :rtype: str
        """
        index = -1
        ret = []
        for s in S:
            index += 1
            a = []
            if (ord(s) >= 33 and ord(s) < 65) or (ord(s) > 90 and ord(s) < 97):
                a.append(index)
                a.append(s)
                S = S.replace(s, "", 1)
                ret.append(a)
        a = list(S)
        a.reverse()
        for i in range(len(ret)):
            a.insert(ret[i][0], ret[i][1])
        return "".join(a)

if __name__ == '__main__':
    S="Test1ng-Leet=code-Q!"
    s=Solution()
    print(s.reverseOnlyLetters(S))





