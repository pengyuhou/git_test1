class Solution(object):
    def diStringMatch(self, S):
        l = len(S)
        a = list(range(l+1))
        ret=[]
        for i in S:
            if i == "I":
                ret.append(a.pop(0))
            else:
                ret.append(a.pop())
        ret += a
        return ret

if __name__ == "__main__":
    s = "DDI"
    print(Solution().diStringMatch(s))


