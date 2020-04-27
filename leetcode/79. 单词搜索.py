"""
给定一个二维网格和一个单词，找出该单词是否存在于网格中。
单词必须按照字母顺序，通过相邻的单元格内的字母构成，其中“相邻”单元格是那些水平相邻或垂直相邻的单元格。同一个单元格内的字母不允许被重复使用。
 board =
[
  ['A','B','C','E'],
  ['S','F','C','S'],
  ['A','D','E','E']
]

给定 word = "ABCCED", 返回 true
给定 word = "SEE", 返回 true
给定 word = "ABCB", 返回 false
"""
class Solution(object):
    def exist(self, board, word):
        def dfs(x,y,mark,index):
            if index >= len(word):
                return True
            for dx,dy in [(0,1),(0,-1),(1,0),(-1,0)]:
                xi = x + dx
                yi = y + dy
                if 0<=xi<m and 0<=yi<n and board[xi][yi]==word[index]:
                    if mark[xi][yi] == 1:
                        continue
                    mark[xi][yi] = 1
                    if dfs(xi,yi,mark,index+1):
                        return True
                    else:
                        mark[xi][yi] = 0
            return False
        m = len(board)
        n = len(board[0])
        mark = [[0 for _ in range(n)] for _ in range(m)]
        for i in range(m):
            for j in range(n):
                index = 0
                if board[i][j]==word[index]:
                    mark[i][j] = 1
                    if dfs(i,j,mark,index+1):
                        return True
                    else:
                        mark[i][j] = 0
        return False

if __name__ == "__main__":
    board =[
            ['A', 'B', 'C', 'E'],
            ['S', 'F', 'C', 'S'],
            ['A', 'D', 'E', 'E']
        ]
    word = "ABCB"

    print(Solution().exist(board,word))