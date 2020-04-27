class Solution(object):
    def combinationSum(self, candidates, target):
        ret = []
        def dfs(p,res):
            if sum(res)>=target:
                a = sorted(res)
                if sum(res)==target and a not in ret:
                    ret.append(a.copy())
                return

            for i in range(len(p)):
                res.append(p[i])
                dfs(p,res)
                res.pop()
        dfs(candidates,[])
        return ret

if __name__ =="__main__":
    candidates = [2,3,5]
    target = 8
    print(Solution().combinationSum(candidates,target))










