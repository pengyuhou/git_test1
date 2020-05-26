class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        l = len(s)
        for i in range(1, len(s)):
            if (c := l // (lx := len(s[:i]))) == l / lx:
                if s[:i] * c == s:
                    return True
        return False


if __name__ == "__main__":
    print(Solution().repeatedSubstringPattern('b'))
