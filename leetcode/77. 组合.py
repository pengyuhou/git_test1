class Solution(object):
    def combine(self, n, k):
        nums = list(range(1, n + 1))
        mark = [False for _ in range(n)]
        ret = []
        def dfs(p, level, res):
            if level == k + 1:
                # a=sorted(res)
                # if a not in ret:
                ret.append(res.copy())
                return
            for i in range(len(p)):
                if not mark[i]:
                    if not res:
                        mark[i] = True
                        res.append(p[i])
                        dfs(p, level + 1, res)
                        mark[i] = False
                        res.pop()
                    if res and p[i]>max(res):
                        mark[i] = True
                        res.append(p[i])
                        dfs(p,level+1,res)
                        mark[i] = False
                        res.pop()
        dfs(nums,1,[])
        return ret




if __name__ == "__main__":
    print(Solution().combine(13, 13))
