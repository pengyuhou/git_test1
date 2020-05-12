class Solution(object):
    def permutation(self, s):
        s = list(s)
        l = len(s)
        mark = [False for _ in range(l)]
        ret = []
        def dfs(p, pd, level, res):
            if level == l + 1:
                ret.append(''.join(res))
                return
            for i in range(l):
                if not pd[i]:
                    pd[i] = True
                    res.append(p[i])
                    dfs(p, pd, level + 1, res)
                    res.pop()
                    pd[i] = False
        dfs(s, mark, 1, [])
        return ret


if __name__ == "__main__":
    print(Solution().permutation(""))
