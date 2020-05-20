class Solution:
    def findTheLongestSubstring(self, s: str) -> int:
        from collections import Counter
        c = Counter()
        ret = [c.copy()]
        distance = 0
        for i in s:
            if i in {'a', 'e', 'i', 'o', 'u'}:
                c[i] += 1
            ret.append(c.copy())
        l = len(ret)
        for i in range(l - 1):
            for j in range(i + 1, l):
                if not any([k % 2 for k in (ret[j] - ret[i]).values()]):
                    distance = max(distance, j - i)
        return distance

if __name__ == "__main__":
    print(Solution().findTheLongestSubstring('eleetminicoworoep'))
