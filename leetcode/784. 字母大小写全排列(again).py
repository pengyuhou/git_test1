"""
深度优先搜索套路：
dfs传入四个参数 p ， pd ,level ,res
p 是输入内容 pd 是标记数组 level 是当前递归进行到的层数 ，res 保存输出结果
对于传入一个数组 则一般引入标记数组 pd 
对于传入一个字符串，则一般引入index

先写dfs的截条件，一般是level到达最大值结合其他判断return

之后遍历候选节点，对有可能的节点逐一遍历，res.append() dfs() res.pop() 回溯
dfs(root)
"""

class Solution(object):
    def letterCasePermutation(self, S):
        l = len(S)
        ret = []

        def dfs(p, index, level, res):
            # 截至条件
            if level == l + 1 or index == l:
                ret.append(''.join(res))
                return
            # 遍历候选节点
            if p[index].isdigit():
                res.append(p[index])
                dfs(p, index + 1, level + 1, res)
                res.pop()

            if p[index].isalpha() and p[index].isupper():
                res.append(p[index])
                dfs(p, index + 1, level + 1, res)
                res.pop()

                res.append(p[index].lower())
                dfs(p, index + 1, level + 1, res)
                res.pop()
            if p[index].isalpha() and p[index].islower():
                res.append(p[index])
                dfs(p, index + 1, level + 1, res)
                res.pop()

                res.append(p[index].upper())
                dfs(p, index + 1, level + 1, res)
                res.pop()

        dfs(S, 0, 1, [])
        return ret


if __name__ == "__main__":
    print(Solution().letterCasePermutation("a1B2"))
