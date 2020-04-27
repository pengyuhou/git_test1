class Solution(object):
    def flipAndInvertImage(self, A):

        for a in A:
            a.reverse()
        ret = []
        for a in A:
            res = []
            for i in a:
                if i == 1:
                    res.append(0)
                else:
                    res.append(1)
            ret.append(res)
        return ret





if __name__ == '__main__':
    A = [[1,1,0],[1,0,1],[0,0,0]]
    s=Solution()
    print(s.flipAndInvertImage([]))







