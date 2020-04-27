class Solution(object):
    def getPermutation(self, n, k):
        a = [str(i) for i in range(1, n + 1)]
        mark = [False for _ in range(n)]
        ret = []

        def dfs(p, pd, level, res):
            if level == n + 1:
                ret.append(''.join(res.copy()))
                return
            for i in range(n):
                if not pd[i]:
                    res.append(p[i])
                    pd[i] = True
                    dfs(p, pd, level + 1, res)
                    res.pop()
                    pd[i] = False

        dfs(a, mark, 1, [])
        return str(sorted([int(i) for i in ret])[k - 1])


if __name__ == "__main__":
    print(Solution().getPermutation(6, 1))
    # chs = list(map(str, range(1, 10)))
    # a=[*(map(str,range(1,10)))]
    a = [(0, 1), (1, 2)]
