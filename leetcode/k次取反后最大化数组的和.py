class Solution:
    def largestSumAfterKNegations(self, A, K) -> int:
        a = sorted(A)
        sub = []
        add = []
        for i in a:
            if i < 0:
                sub.append(i)
            else:
                add.append(i)
        x=len(sub)

        if not sub == [] and x >= K:

            for i in range(K):
                sub[i] = -sub[i]
            return sum(sub + add)

        if (not sub == [] and x < K) and 0 in A:

            for i in range(x):
                sub[i] = -sub[i]
            return sum(sub + add)

        if (not sub == [] and x < K) and 0 not in A and (K-x)%2 !=0:

            for i in range(x):
                sub[i] = -sub[i]
            if add[0] > sub[-1]:
                sub[-1] = -sub[-1]
            else:
                add[0] = -add[0]

            return sum(sub + add)
        if (not sub == [] and x < K) and 0 not in A and (K - x) % 2 == 0:
            for i in range(x):
                sub[i] = -sub[i]
            return sum(sub + add)

        if sub == [] and K % 2:
            add[0] = -add[0]
            return sum(add)
        if sub == [] and not K % 2:
            return sum(add)


if __name__ == '__main__':
    A=[-2, 9, 9, 8, 4]
    K=5
    s=Solution()
    print(s.largestSumAfterKNegations(A,K))





















