class Solution:
    def translateNum(self, num: int) -> int:
        word = list('abcdefghijklmnopqrstuvwxyz')
        num_list = list(range(26))
        a = {}
        for i, j in zip(num_list, word):
            a[i] = j
        l = len(str(num))
        num = str(num)
        ret = []
        def dfs(p, index, res):
            if index >= l:
                add=''.join(res.copy())
                if add not in ret:
                    ret.append(add)
                return
            for i in range(1, 3):
                tmp = p[index:index + i]
                if 0 <= int(tmp) < 26 and not tmp.startswith('0') or tmp=='0':
                    index = index + i
                    res.append(a[int(tmp)])
                    dfs(p,index,res)
                    res.pop()
                    index = index - i
        dfs(num,0,[])
        return len(ret)




if __name__ == "__main__":
    print(Solution().translateNum(506))
    a=[1,2,3]

