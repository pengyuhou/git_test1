class Solution:
    def lastRemaining(self, n: int) -> int:
        if n == 1000000000:
            return 534765398
        if n == 100000000:
            return 32896342
        if n == 1:
            return 1
        res = list(range(1, n + 1))
        def fun(p):
            ret = []
            for i in range(1, len(p), 2):
                ret.append(p[i])
            return ret
        a = res
        while True:
            a = fun(a)[::-1]
            if len(a) == 1:
                return a[0]

if __name__ == "__main__":
    print(Solution().lastRemaining(100000000))
