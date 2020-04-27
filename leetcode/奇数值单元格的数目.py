class Solution(object):
    def oddCells(self, n, m, indices):
        """
        :type n: int
        :type m: int
        :type indices: List[List[int]]
        :rtype: int
        """
        ret = []
        for i in range(n):
            a = []
            for j in range(m):
                a.append(0)
            ret.append(a)
        print(ret)
        for indice in indices:
            r = indice[0]
            c = indice[1]
            for i in range(len(ret[r])):
                ret[r][i] += 1
            for j in ret:
                j[c] += 1

        index = 0
        for i in ret:
            for j in i:
                if j % 2:
                    index += 1
        return index

if __name__ == '__main__':
    n,m=2,3

    indices = [[0, 1], [1, 1]]

    S=Solution()
    print(S.oddCells(n,m,indices))

    # ret=[]
    # for i in range(n):
    #     a=[]
    #     for j in range(m):
    #         a.append(0)
    #     ret.append(a)
    # print(ret)
    # for indice in indices:
    #     r=indice[0]
    #     c=indice[1]
    #     for i in range(len(ret[r])):
    #         ret[r][i] += 1
    #     for j in ret:
    #         j[c] += 1
    #
    # index=0
    # for i in ret:
    #     for j in i:
    #         if j%2:
    #             index += 1
    # print(index)








