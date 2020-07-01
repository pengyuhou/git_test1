class Solution(object):
    def allPathsSourceTarget(self, graph):
        """
        :type graph: List[List[int]]
        :rtype: List[List[int]]
        """
        n = len(graph)
        ret = []

        def dfs(p, index, res):
            if index == n - 1:
                # res += [index]
                ret.append(res[:]+[index])
                return
            for i in p[index]:
                res.append(index)
                dfs(p, i, res)
                res.pop()

        dfs(graph, 0, [])
        return ret


print(Solution().allPathsSourceTarget([[1, 2], [3], [3], []]))
