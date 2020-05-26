class Solution:
    k = 0
    def removeKdigits(self, x: str, res: int) -> str:
        self.k = res
        def fun(num):
            stack = []
            flag = True
            for i in range(len(num)):
                if not stack:
                    stack.append(num[i])
                    continue
                if flag and self.k > 0 and int(num[i]) < int(stack[-1]):
                    stack.pop()
                    stack.append(num[i])
                    self.k -= 1
                    flag = False
                    continue
                stack.append(num[i])
            return stack
        while self.k:
            l1 = len(x)
            x = ''.join(fun(x))
            x = x.lstrip('0')
            if len(x) == l1:
                return x[:-self.k] if len(x[:-self.k]) else '0'
        return x if x else '0'

if __name__ == "__main__":
    print(Solution().removeKdigits('112', 2))
