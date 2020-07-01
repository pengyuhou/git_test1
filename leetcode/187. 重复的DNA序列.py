class Solution(object):
    def findRepeatedDnaSequences(self, s):
        from collections import defaultdict
        d = defaultdict(int)
        for i in range(x := len(s)):
            if i + 10 <= x:
                d[s[i:i + 10]] += 1
        return list(dict(list(filter(lambda x: x[1] > 1, d.items()))).keys())


print(Solution().findRepeatedDnaSequences(s="AAAAAAAAAAA"))
