class Solution(object):
    def imageSmoother(self, M):
        mat=M
        hang = len(mat)
        lie = len(mat[0])
        ret = []
        for i in range(hang):
            a = []
            for j in range(lie):
                a.append(None)
            ret.append(a)
        if hang==1 and lie==1:
            return mat
        if hang == 1 and lie != 1:
            for i in range(len(ret[0])):
                if i == 0:
                    ret[0][i] = (mat[0][i] + mat[0][i + 1]) // 2
                if i == len(ret[0]) - 1:
                    ret[0][i] = (mat[0][i] + mat[0][i - 1]) // 2
                if i != 0 and i != len(ret[0]) - 1:
                    ret[0][i] = (mat[0][i] + mat[0][i + 1] + mat[0][i - 1]) // 3
        if lie == 1 and hang != 1:
            for i in range(len(ret)):
                if i == 0:
                    ret[i][0] = (mat[i][0] + mat[i + 1][0]) // 2
                elif i == len(ret) - 1:
                    ret[i][0] = (mat[i][0] + mat[i - 1][0]) // 2
                else:
                    ret[i][0] = (mat[i][0] + mat[i - 1][0] + mat[i + 1][0]) // 3

        if hang > 1 and lie > 1:
            for i in range(hang):
                for j in range(lie):
                    if i == 0 and j == 0:
                        ret[0][0] = (mat[0][0] + mat[0][1] + mat[1][0] + mat[1][1]) // 4
                    elif i == hang - 1 and (j != 0 and j != lie - 1):
                        ret[i][j] = (mat[i][j] + mat[i][j + 1] + mat[i][j - 1] + mat[i - 1][j] + mat[i - 1][j + 1] +
                                     mat[i - 1][j - 1]) // 6

                    elif i == 0 and j == lie - 1:
                        ret[0][j] = (mat[0][j] + mat[0][j - 1] + mat[1][j] + mat[1][j - 1]) // 4

                    elif i == hang - 1 and j == 0:
                        ret[hang - 1][0] = (mat[hang - 1][0] + mat[hang - 1][1] + mat[hang - 2][0] + mat[hang - 2][
                            1]) // 4

                    elif i == hang - 1 and j == lie - 1:
                        ret[hang - 1][lie - 1] = (mat[hang - 1][lie - 1] + mat[hang - 1][lie - 2] + mat[hang - 2][
                            lie - 2] + mat[hang - 2][lie - 1]) // 4

                    elif i == 0 and (j != 0 and j != lie - 1):
                        ret[0][j] = (mat[0][j] + mat[0][j + 1] + mat[0][j - 1] + mat[1][j] + mat[1][j + 1] + mat[1][
                            j - 1]) // 6
                    elif j == 0 and (i != 0 and i != hang - 1):
                        ret[i][j] = (mat[i][j] + mat[i - 1][j] + mat[i + 1][j] + mat[i][j + 1] + mat[i - 1][1] +
                                     mat[i + 1][1]) // 6

                    elif j == lie - 1 and (i != 0 and i != hang - 1):
                        ret[i][j] = (mat[i][j] + mat[i - 1][j] + mat[i + 1][j] + mat[i][j - 1] + mat[i - 1][j - 1] +
                                     mat[i + 1][j - 1]) // 6

                    elif i != 0 and i != hang - 1 and j != 0 and j != lie - 1:
                        ret[i][j] = (mat[i][j] + mat[i][j + 1] + mat[i][j - 1] + mat[i - 1][j] + mat[i - 1][j - 1] +
                                     mat[i - 1][j + 1] + mat[i + 1][j] + mat[i + 1][j - 1] + mat[i + 1][j + 1]) // 9
        return ret

if __name__ == "__main__":
    mat=[[2,3,4],[5,6,7],[8,9,10],[11,12,13],[14,15,16]]
    mat=[[1,1,3]]
    # mat=[[1, 1, 1],
    #     [1, 0, 1],
    #     [1, 1, 1]]
    mat = [[1,1,1],[1,0,1]]
    mat=[[1]]
    print(Solution().imageSmoother(mat))








