class Solution:
    def fun(self, a):
        x = a[0]
        y = a[1]
        for i in range(2, len(a)):
            if x + y == a[i]:
                x, y = y, x + y
            else:
                return False
        return True

    def isAdditiveNumber(self, num: str) -> bool:

        l = len(num)
        def dfs(p, index, res):
            if index == l:
                if len(res) >= 3 and len(''.join([str(i) for i in res])) == l and self.fun(res[:]):
                    return True
                return False
            for i in range(index + 1, l + 1):
                res.append(int(p[index:i]))
                if dfs(p, i, res):
                    return True
                res.pop()
            return False


        return dfs(num, 0, [])



if __name__ == "__main__":
    print(Solution().isAdditiveNumber("101123581321345589144"))
