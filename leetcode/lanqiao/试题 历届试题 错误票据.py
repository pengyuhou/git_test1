class Solution:
    def __init__(self):
        self.line = int(input())
        self.ret = []
        for _ in range(self.line):
            a = input()
            a.strip()
            res = [int(i) for i in a.split()]
            self.ret += res

    def fun(self):
        res = [None,None]
        self.ret.sort()
        for i, j in enumerate(self.ret, start=self.ret[0]):
            if self.ret.count(j) > 1 and j not in res:
                res[1] = j
            if i != j and i not in self.ret:
                res[0] = i
        return res


print(*Solution().fun())
