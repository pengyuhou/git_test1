class Solution(object):
    def findTheDifference(self, s, t):
        for i in s:
            if i in t:
                t=t.replace(i,'',1)
        return t


if __name__ == "__main__":
    s = "a"
    t = "aa"
    print(t.replace(s, '',1))
    # for i in s:
    #     if i in t:
    #         t=t.replace(i,"")
    # print(t)
    # s1=Solution()
    # print(s1.findTheDifference(s, t))










