class Solution(object):
    def countCharacters(self, words, chars):
        """
        :type words: List[str]
        :type chars: str
        :rtype: int
        """
        ret = []
        for word in words:
            chars_ = chars
            index = 0
            for i in word:
                if i not in chars_:
                    break
                if i in chars_:
                    index += 1
                    chars_ = chars_.replace(i, '', 1)
            if index == len(word):
                ret.append(word)
        return len("".join(ret))


if __name__ == '__main__':
    words = ["hat", "bt", "cat", "tree"]
    chars = "atach"
    # words=['tree']
    # words = ["hello", "world", "leetcode"]
    s=Solution()
    print(s.countCharacters(words,chars))



    # ret=[]
    # for word in words:
    #     chars = "atach"
    #     index = 0
    #     for i in word:
    #         if i not in chars:
    #
    #             break
    #         if i in chars:
    #             index += 1
    #             chars=chars.replace(i,'',1)
    #     if index == len(word):
    #         ret.append(word)
    # print(len("".join(ret)))






