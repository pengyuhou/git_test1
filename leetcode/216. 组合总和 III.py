class Solution(object):
    def combinationSum3(self, k, n):
        """
        :type k: int
        :type n: int
        :rtype: List[List[int]]
        """
        a = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        pd = [False for _ in range(9)]
        ret = []

        def dfs(p, pd, level, res):
            if sum(res) >= n and level == k + 1:
                a = sorted(res)
                if sum(res) == n and a not in ret:
                    ret.append(a)
                return
            for i in range(len(p)):
                if not pd[i]:
                    pd[i] = True
                    res.append(p[i])
                    dfs(p, pd, level + 1, res)
                    res.pop()
                    pd[i] = False

        dfs(a, pd, 1, [])
        return ret


if __name__ == "__main__":
    print(Solution().combinationSum3(3, 7))
