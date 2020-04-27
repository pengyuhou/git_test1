class Solution(object):
    def transpose(self, A):
        a=A
        ret = []
        for i in range(len(a[0])):
            res = []
            for j in range(len(a)):
                res.append(0)
            ret.append(res)

        for i in range(len(a)):
            for j in range(len(a[0])):
                ret[j][i] = a[i][j]
        return ret
import numpy as np
if __name__ == '__main__':
    a=[[1,2,3],[4,5,6]]



















