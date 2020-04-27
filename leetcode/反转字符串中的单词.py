class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        ret = s.split(' ')
        k = []
        for word in ret:
            a = []
            ll=len(word)
            for i in range(ll):
                res = word[i].replace(word[i], word[ll - 1 - i], 1)
                a.append(res)
            r = ''.join(a)
            k.append(r)

        return ' '.join(k)

if __name__ == '__main__':
    s="Let's take LeetCode contest"
    q=Solution()
    print(q.reverseWords(s))

    # ret=s.split(' ')
    # k=[]
    # for word in ret:
    #
    #
    #     s=word
    #     a=[]
    #     for i in range(len(s)):
    #
    #         res=s[i].replace(s[i], s[len(s) - 1 - i], 1)
    #         a.append(res)
    #     r=''.join(a)
    #     k.append(r)
    # print(k)
    # print(' '.join(k))





















