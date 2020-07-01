class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str] 
        """
        a = ['(', ')']
        ret = []
        def dfs(res):
            if len(res) == 2 * n :
                if res.count('(') == res.count(')'):
                    if ''.join(res.copy()) not in ret:
                        ret.append(''.join(res.copy()))
                return
            for i in a:
                if res.count('(')==res.count(')'):
                    res.append('(')
                    dfs(res)
                    res.pop()
                else:
                    res.append(i)
                    dfs(res)
                    res.pop()
        dfs([])
        return ret




if __name__ == "__main__":
    print(Solution().generateParenthesis(3))
