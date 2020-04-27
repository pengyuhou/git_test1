class Solution(object):
    def detectCapitalUse(self, word):
        """
        :type word: str
        :rtype: bool
        """
        s=word
        if s[0].isupper() and s[1:].islower():
            return True
        if s.isupper() or s.islower():
            return True
        return False

            # for i in range(len(word)):
            #
            #     if word[i].isupper():
            #         index_U += 1
            #     if word[i].islower():
            #         index_L += 1
            #
            # if index_U == len(word):
            #     print(word)
            # if index_L == len(word):
            #     print(word)

if __name__ == '__main__':
    import time

    print(time.localtime())
    # word = "DASDAa"
    # index_U = 0
    # index_L = 0
    # s='asdasf'
    # s=Solution()
    # print(s.detectCapitalUse(word))











