class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        s = list(s)
        ret = []
        l = 0
        for i in s:
            if i not in ret:
                ret.append(i)
            else:
                ret.append(i)
                ret = ret[ret.index(i)+1:]
            l = max(l, len(ret))
        return l

if __name__ == "__main__":
    print(Solution().lengthOfLongestSubstring('abcabcbb'))

























