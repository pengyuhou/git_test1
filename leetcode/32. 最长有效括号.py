class Solution:
    def longestValidParentheses(self, s: str) -> int:
        stack = []
        s = list(enumerate(s))
        mark = [0] * len(s)
        for i in s:
            stack.append(i)
            if i[1] == ')' and len(stack) > 1 and stack[-2][1] == '(':
                stack.pop()
                stack.pop()
        for i in stack:
            mark[i[0]] = 1
        ret = -float('inf')
        for i in range(len(mark)):
            cnt = 0
            while i < len(mark) and mark[i] == 0:
                cnt += 1
                i += 1
            i += 1
            ret = max(ret, cnt)
        return ret if ret != -float('inf') else 0


print(Solution().longestValidParentheses(")()())"))
