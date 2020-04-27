class Solution(object):
    def findOcurrences(self, text, first, second):
        """
        :type text: str
        :type first: str
        :type second: str
        :rtype: List[str]
        """
        a = text.split()
        ret = []
        l = len(a)
        for i in range(l):
            if i + 1 < l and i + 2 < l:
                if a[i] == first and a[i + 1] == second:
                    ret.append(a[i + 2])
        return ret


if __name__ == "__main__":
    text = "alice is a good girl she is a good student"
    first = "a"
    second = "good"
    print(Solution().findOcurrences(text,first,second))









