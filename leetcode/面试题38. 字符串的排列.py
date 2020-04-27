class Solution(object):
    def permutation(self, s):
        p = list(s)
        l = len(s)
        pd = [False for _ in range(l)]
        ret = []

        def dfs(p, pd, level, res):
            if level == l + 1:
                ret.append(''.join(res.copy()))
                return
            for i in range(l):
                if not pd[i]:
                    pd[i] = True
                    res.append(p[i])
                    dfs(p, pd, level + 1, res)
                    pd[i] = False
                    res.pop()

        dfs(p, pd, 1, [])
        return list(set(ret))


if __name__ == "__main__":
    print(Solution().permutation("abc"))
