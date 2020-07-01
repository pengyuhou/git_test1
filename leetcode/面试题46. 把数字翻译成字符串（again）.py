class Solution:
    def translateNum(self, num: int) -> int:
        word = list(enumerate('abcdefghijklmnopqrstuvwxyz'))
        num = str(num)
        l = len(num)
        ret = []

        def dfs(p, index, res):
            if index >= l:
                if res not in ret:
                    ret.append(res.copy())
                return
            for i in range(1, 3):
                item = int(p[index:index + i])
                if (0 <= item <= 25 and not p[index:index + i].startswith('0')) or p[index:index + i] == '0':
                    res.append(item)
                    dfs(p, index + i, res)
                    res.pop()

        dfs(num, 0, [])
        word = dict(word)
        res = ret
        ret = []
        for i in res:
            tmp = ''
            for j in i:
                tmp += word[j]
            ret.append(tmp)
        print(ret)
        return len(ret)


print(Solution().translateNum(56734513411321))
print(56734513411321>2**31)
