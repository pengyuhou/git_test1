class Solution(object):
    def kWeakestRows(self, mat, k):
        """
        :type mat: List[List[int]]
        :type k: int
        :rtype: List[int]
        """
        ret = []
        for i in range(len(mat)):
            t = [i]
            count = 0
            for j in mat[i]:
                if j == 0:
                    break
                count += 1
            t.append(count)
            ret.append(t)
        a = sorted(ret, key=lambda x: x[1])
        print(a)
        b = [i[0] for i in a[:k]]
        return b
if __name__ == "__main__":
    mat =[[1,0,0,0],
 [1,1,1,1],
 [1,0,0,0],
 [1,0,0,0]]
    k = 2

    print(b)




