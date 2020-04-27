class Solution(object):
    def isIsomorphic(self, s, t):
        if len(s)==len(t):
            index = 0
            l = len(s)
            a={}
            while index<l:
                if s[index] not in a.keys():

                    a[s[index]]=t[index]
                else:
                    if a[s[index]]!=t[index]:
                        return False
                index += 1
            if len(set(a.values()))==len(a.values()):
                return True
            else:
                return False
        else:
            return False

if __name__ == "__main__":
    s = "ab"
    t = "aa"
    s = "foo"
    t = "bar"
    s = "paper"
    t = "title"
    s='baa'
    t='baa'
    s='ab'
    t='ca'
    print(Solution().isIsomorphic(s,t))



