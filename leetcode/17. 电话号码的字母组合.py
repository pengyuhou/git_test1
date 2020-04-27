class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        if digits=='':
            return []
        num = ['2', '3', '4', '5', '6', '7', '8', '9']
        b = [list('abc'), list('def'), list('ghi'), list('jkl'), list('mno'), list('pqrs'), list('tuv'), list('wxyz')]
        a = {i: j for i, j in zip(num, b)}
        ret = []
        def dfs(p, index, level, res):
            if level == len(digits) + 1:
                ret.append(''.join(res))
                return
            for i in range(len(a[p[index]])):
                res.append(a[p[index]][i])
                dfs(p, index + 1, level + 1, res)
                res.pop()
        dfs(digits,0,1,[])
        return ret


if __name__ == "__main__":
    print(Solution().letterCombinations("23"))

