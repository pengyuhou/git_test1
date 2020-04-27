"""
ABC
深度优先搜索
"""

ret=[]
def dfs(p,pb,level,res):
    # 截至条件
    if level==len(p)+1:
        a = res.copy()
        ret.append(a)
        return
#     遍历候选节点
    for i in range(len(p)):
        c = p[i]
        if not pb[i]:
            res.append(c)
            pb[i]=True
            dfs(p,pb,level+1,res)
            res.pop()
            pb[i]=False
p=['A','B','C']
pb = [False,False,False]
res=[]
dfs(p,pb,1,res)
print(ret)




















