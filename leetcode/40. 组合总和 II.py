class Solution(object):
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        l = len(candidates)
        pd = [False for _ in range(l)]
        ret = []

        def dfs(p, pd, res):
            if sum(res) >= target:
                a = sorted(res)

                if sum(res) == target and a not in ret:
                    ret.append(a)
                return
            for i in range(len(p)):
                if not pd[i]:
                    pd[i] = True
                    res.append(p[i])
                    dfs(p, pd, res)
                    pd[i] = False
                    res.pop()

        dfs(candidates, pd, [])
        return ret


if __name__ == "__main__":
    candidates = [2, 5, 2, 1, 2]
    target = 5
    print(Solution().combinationSum2(candidates, target))
