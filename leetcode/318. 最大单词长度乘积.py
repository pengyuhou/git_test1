class Solution(object):
    def maxProduct(self, words):
        def fun(a, b):
            return not bool(set(a) & set(b))
        res = sorted(words, key=len)
        ret = -float('inf')
        for i in range((x := len(res)) - 1):
            for j in range(i + 1, x):
                if fun(words[i], words[j]):
                    ret = max(ret, len(words[i]) * len(words[j]))
        return ret


print(Solution().maxProduct(["abcw", "baz", "foo", "bar", "xtfn", "abcdef"]))
