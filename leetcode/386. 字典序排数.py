class Solution:
    def lexicalOrder(self, n):
        ret = []
        def dfs(num):
            if num > n:
                return
            ret.append(num)
            for x in range(0, 10):
                dfs(num * 10 + x)
        for i in range(1, 10):
            dfs(i)
        return ret


if __name__ == "__main__":
    print(Solution().lexicalOrder(13))
