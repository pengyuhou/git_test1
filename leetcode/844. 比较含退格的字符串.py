class Solution:
    def backspaceCompare(self, S: str, T: str) -> bool:
        l_s = len(S)
        s = list(S)
        for i in range(l_s - 1, -1, -1):
            if s[i] == '#':
                s[i] = '*'
                k = i-1
                while k >= 0:
                    if s[k] != '#' and s[k]!='*':
                        s[k] = '*'
                        break
                    k -= 1
        ret_s = ''.join([i for i in s if i != '*'])
        l_t = len(T)
        t = list(T)
        for i in range(l_t - 1, -1, -1):
            if t[i] == '#':
                t[i] = '*'
                k = i - 1
                while k >= 0:
                    if t[k] != '#' and t[k] != '*':
                        t[k] = '*'
                        break
                    k -= 1
        ret_t = ''.join([i for i in t if i != '*'])
        return ret_s==ret_t


if __name__ == "__main__":
    s = "aaab####"
    t = "c#d#"
    print(Solution().backspaceCompare(s,t))








