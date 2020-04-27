class Solution(object):
    def mostCommonWord(self, paragraph, banned):
        """
        :type paragraph: str
        :type banned: List[str]
        :rtype: str
        """
        paragraph = paragraph.lower()
        paragraph = paragraph.replace(',', ' ', -1)
        paragraph = paragraph.replace('!', ' ', -1)
        paragraph = paragraph.replace("'", ' ', -1)
        paragraph = paragraph.replace(".", ' ', -1)
        paragraph = paragraph.replace("?", ' ', -1)
        paragraph = paragraph.replace(";", ' ', -1)
        ret = paragraph.split()
        a = {}
        for i in ret:
            if i not in a.keys():
                a[i] = 1
            else:
                a[i] += 1
        res = sorted(a.keys(), key=lambda x: a[x], reverse=True)
        for i in res:
            if i not in banned:
                return i


# !?',;.
if __name__ == "__main__":
    paragraph = "Bob hit a ball, the hit BALL flew far after it was hit."
    banned = ["hit"]
    paragraph = "a, a, a, a, b,b,b,c, c"
    banned=["a"]
    print(Solution().mostCommonWord(paragraph,banned))















