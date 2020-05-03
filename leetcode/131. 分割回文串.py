class Solution(object):
    def ok(self,s):
        l = len(s)
        mid = (l-1)//2
        if l%2:
            if list(s)[:mid] == list(s)[mid+1:][::-1]:
                return True
            else:
                return False
        else:
            if list(s)[:mid+1] == list(s)[mid+1:][::-1]:
                return True
            else:
                return False

    def partition(self, s):
        l = len(s)
        ret = []
        def dfs(p, index, res):
            if index >= l:
                ret.append(res.copy())
                return
            for i in range(index+1,l+1):
                res.append(p[index:i])
                if self.ok(res[-1]):
                    dfs(p, i, res)
                res.pop()
        dfs(s,0,[])
        return ret

if __name__ == "__main__":
    # print(Solution().ok('acffca'))

    print(Solution().partition(""))
