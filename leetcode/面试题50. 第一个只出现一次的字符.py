class Solution:
    def firstUniqChar(self, s: str) -> str:
        l = len(s)
        s = list(s)
        a = set(s)
        ret = []
        for i in a:
            if s.count(i) == 1:
                ret.append(i)
        if  ret:
            min_num = l - 1
            for r in ret:
                if s.index(r) < min_num:
                    min_num = s.index(r)
            return s[min_num]
        else:
            return ' '



if __name__ == "__main__":
    s = ""
    print(Solution().firstUniqChar(s))









