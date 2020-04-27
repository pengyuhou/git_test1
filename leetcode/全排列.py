A = ['A', 'B', 'C', 'D']
pd = [False, False, False, False]


def dfs(p, pd, level, res):
    # 截至条件
    if level == 5:
        print(res)
        return
        # 遍历
    for i in range(len(A)):
        if not pd[i]:
            res.append(A[i])
            pd[i] = True
            dfs(p, pd, level + 1, res)
            res.pop()
            pd[i] = False

dfs(A,pd,1,[])




