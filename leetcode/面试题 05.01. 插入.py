class Solution(object):
    def insertBits(self, N, M, i, j):
        n = list(str(N))
        m = list(str(M))
        l_m = len(m)
        l_n = len(n)
        if l_n < l_m:
            for i in range(l_m - l_n):
                n.append('0')
            l_n = len(n)

        for p in range(l_m):
            n[l_n - 1 - j + p] = m[p]

        return int(''.join(n))


if __name__ == "__main__":
    N = 10000000000
    M = 10011
    i = 2
    j = 6
    N = 1024
    M = 19
    i = 2
    j = 6

    print(Solution().insertBits(N,M,i,j))






