class Solution:
    def decodeString(self, x: str) -> str:
        def fun(s):
            stack = []
            left = 0
            right = 0
            for i in range(len(s)):
                if s[i] == '[' and not stack:
                    left = i
                    stack.append(s[i])
                    continue
                if s[i] == '[':
                    stack.append(s[i])
                if s[i] == ']':
                    stack.pop()
                    if not stack:
                        right = i
                        break
            index = None
            for i in range(left - 1, -1, -1):
                if not s[i].isdigit():
                    index = i
                    break
            if index is None:
                index = -1
            ret = s[:index+1] + int(s[index+1:left]) * s[left + 1:right] + s[right + 1:]
            return ret
        def dfs(p):
            if '[' not in p:
                return p
            res = fun(p)
            return dfs(res)
        return dfs(x)


if __name__ == "__main__":
    print(Solution().decodeString("100[leetcode]"))
