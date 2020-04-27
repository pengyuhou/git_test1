class Solution(object):
    def fun(self):
        n, k = [int(i) for i in input().split()]
        ret = []
        for _ in range(n):
            ret.append(int(input()))
        count = 0
        if k == 1:
            num = 1
            for i in range(1,len(ret)+1):
                num *= i
            return num

        for i in range(len(ret)):
            offset = 0
            while i + offset <= len(ret):
                val = sum(ret[i:i + offset])
                if val == 0:
                    offset += 1
                    continue
                if val % k == 0:
                    count += 1
                offset += 1
        return count
print(Solution().fun())
