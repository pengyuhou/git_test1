class Solution:
    def licenseKeyFormatting(self, S: str, K: int) -> str:
        S = list(S)
        for i in range(len(S)):
            if S[i].isalnum():
                S[i] = S[i].upper()
        S = ''.join(S)
        res = S.split('-')
        res = [i for i in res if i]
        stack = []
        res = list(''.join(res))[::-1]
        ret = []
        for i in range(len(res)):
            stack.append(res[i])
            if len((x := ''.join(stack))) == K:
                ret.append(x[::-1])
                stack.clear()
        if stack:
            stack = [''.join(stack[::-1])]
            ret += stack
        return '-'.join(ret[::-1])


if __name__ == "__main__":
    print(Solution().licenseKeyFormatting(S = "2-5g-3-J", K = 2))
