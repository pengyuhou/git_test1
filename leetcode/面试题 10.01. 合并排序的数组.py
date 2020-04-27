class Solution(object):
    def merge(self, A, m, B, n):
        a = A
        b = B
        ret = []
        index1 = 0
        index2 = 0
        while index1 < m and index2 < n:
            if a[index1]<b[index2]:
                ret.append(a[index1])
                index1 += 1
                continue
            if a[index1] >b[index2]:
                ret.append(b[index2])
                index2 += 1
                continue
            if a[index1] == b[index2]:
                ret.append(a[index1])
                ret.append(b[index2])
                index2 += 1
                index1 += 1
                continue
        if index1>=m and index2<=n:
            ret += b[index2:n]
        if index2>=n and index1<=m:
            ret += a[index1:m]
        A[:] = ret


if __name__ == "__main__":
    A = [1]
    m = 1
    B = []
    n = 0
    print(Solution().merge(A,m,B,n))






