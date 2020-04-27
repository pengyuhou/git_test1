class Solution(object):
    def findString(self, words, s):
        """
        :type words: List[str]
        :type s: str
        :rtype: int
        """
        try:
            return words.index(s)

        except:
            return -1

if  __name__ == "__main__":
    words = ["at", "", "", "", "ball", "", "", "car", "", "", "dad", "", ""]
    s = "at"
    print(Solution().findString(words,s))
    # print(words.index(s))

