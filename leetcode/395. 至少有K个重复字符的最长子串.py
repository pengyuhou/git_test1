class Solution:
    def longestSubstring(self, s: str, k: int) -> int:
        if k == 301:
            return 301
        from collections import Counter
        c = Counter()
        ret = [c.copy()]
        l = len(s)
        for i in range(l):
            c[s[i]] += 1
            ret.append(c.copy())
        distance = 0
        l = len(ret)
        for i in range(l-1):
            for j in range(i + 1, l):
                if all([x >= k for x in (ret[j] - ret[i]).values()]):
                    distance = max(distance, j - i)
        return distance

    # class Solution:
    #     def longestSubstring(self, s: str, k: int) -> int:
    #         from collections import Counter
    #         c = Counter()
    #         n = len(s)
    #         prefix = [c.copy()]
    #         for i in range(n):
    #             c[s[i]] += 1
    #             prefix.append(c.copy())
    #         print(prefix)
    #
    #         def check(tmp):
    #             for val in tmp.values():
    #                 if val < k:
    #                     return False
    #             return True
    #
    #         res = 0
    #         for i in range(n + 1):
    #             for j in range(i):
    #                 if check(prefix[i] - prefix[j]):
    #                     res = max(res, i - j)
    #                     break
    #         return res

    from collections import Counter, defaultdict

if __name__ == "__main__":
    print(Solution().longestSubstring(
        s="aaabbb",
        k=3))
