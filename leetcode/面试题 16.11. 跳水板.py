# class Solution(object):
#     def divingBoard(self, shorter, longer, k):
#         if not k:
#             return []
#         ret = set()
#         num = k * longer
#         for i in range(k+1):
#             ret.add(num)
#             num = num - longer + shorter
#         return list(ret)


class Solution(object):
    def divingBoard(self, shorter, longer, k):
        if not k:
            return []
        import functools
        @functools.lru_cache(None)
        def dfs(num):
            if num == 1:
                return [shorter, longer]
            res = dfs(num - 1)
            ret1 = map(lambda x: x + shorter, res)
            ret2 = map(lambda x: x + longer, res)
            return set(list(ret1) + list(ret2))
        return sorted(dfs(k))


print(Solution().divingBoard(7, 3625, 1000))
