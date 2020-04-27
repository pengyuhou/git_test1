class Solution:
    def isSubStructure(self, A: TreeNode, B: TreeNode) -> bool:
        ret1 = []
        ret2 = []
        if not A or not B:
            return False
        def dfs(node,res,ret):
            if not node :
                if res not in ret:
                    ret.append(res.copy())
                return
            res.append(str(node.val))
            dfs(node.left,res,ret)
            dfs(node.right,res,ret)
            res.pop()
        dfs(A,[],ret1)
        dfs(B,[],ret2)
        ans1=[]
        ans2 = []
        for i in range(len(ret1)):
            ans1.append(''.join(ret1[i]))
        for j in range(len(ret2)):
            ans2.append(''.join(ret2[j]))
        for i in ans2:
            flag = True
            for j in ans1:
                if i in j:
                    flag = False
                    break
            if flag:
                return False
        return True



a= ['124', '12', '13']
b= ['3']
for b_ in b:
    for a_ in a:
        if b_ in a_:
            break

