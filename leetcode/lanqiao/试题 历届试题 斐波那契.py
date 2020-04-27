class Solution:
    def fun(self):
        s = input()
        n, m, p = [int(i) for i in s.split()]
        max_val = max(n, m)
        ret = [None for _ in range(max_val)]

        for i in range(len(ret)):
            if i == 0 or i == 1:
                ret[i] = 1
            else:
                ret[i] = ret[i - 1] + ret[i - 2]

        return sum(ret[:n]) % ret[m - 1] % p


print(Solution().fun())
