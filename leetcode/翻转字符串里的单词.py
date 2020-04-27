class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        s_l = len(s)
        c = ''
        ret = []
        for i in range(s_l):

            if s[i] is not ' ':
                c += s[i]
            if not s[i] is not ' ':
                c = ''
            if i != s_l - 1:
                if s[i] is not ' ' and not s[i + 1] is not ' ':
                    ret.append(c)
            else:
                if s[i] is not ' ':
                    ret.append(c)
        ret.reverse()
        res=" ".join(ret)
        return res

if __name__ == '__main__':
    s="the sky is blue"
    s1=Solution()
    print(s1.reverseWords(s))













