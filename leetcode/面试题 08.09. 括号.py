class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        ret = []
        def dfs(res,level):
            if level== 2 * n+1:
                if res.count('(') == res.count(')') and ''.join(res) not in ret:
                    ret.append(''.join(res.copy()))
                return
            if res.count('(') == res.count(')'):
                res.append('(')
                dfs(res,level+1)
                res.pop()
            else:
                res.append('(')
                dfs(res,level+1)
                res.pop()
                res.append(')')
                dfs(res,level+1)
                res.pop()
        dfs([],1)
        return ret


if __name__ == "__main__":
    print(Solution().generateParenthesis(3))
