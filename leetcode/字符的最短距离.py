class Solution(object):
    def shortestToChar(self, S, C):
        s=S
        c=C
        l = len(s)
        ret = [None] * l

        for i in range(len(s)):
            if s[i] == c:
                ret[i] = 0
        r = 1
        l=len(ret)
        while None in ret:
            for i in range(l):
                if ret[i] == 0:
                    if i + r <= l - 1 and i - r >= 0:
                        if ret[i + r] == None:
                            ret[i + r] = r
                        if ret[i - r] == None:
                            ret[i - r] = r
                    if i + r > l - 1 and i - r >= 0:
                        if ret[i - r] == None:
                            ret[i - r] = r
                    if i + r <= l - 1 and i - r < 0:
                        if ret[i + r] == None:
                            ret[i + r] = r
            r += 1
        return ret

if __name__ =="__main__":
    s = "loveleetcode"
    c = 'e'
    print(Solution().shortestToChar(s,c))






