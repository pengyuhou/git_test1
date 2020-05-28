class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        from collections import Counter
        l = len(s1)
        c = Counter()
        c1 = Counter()
        for j in range(l):
            c1[s1[j]] += 1
        ret = [c.copy()]
        for i in range(len(s2)):
            c[s2[i]] += 1
            ret.append(c.copy())
        for i in range(lx := len(ret)):
            if i + l < lx and sorted((ret[i + l] - ret[i]).items()) == sorted(c1.items()):
                return True
        return False


from collections import Counter

print(Solution().checkInclusion("adc",
                                "dcda"))
