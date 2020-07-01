class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        v1 = version1.split('.')
        v2 = version2.split('.')
        l1, l2 = len(v1), len(v2)
        if l1 > l2:
            v2 += ['0'] * (l1 - l2)
        else:
            v1 += ['0'] * (l2 - l1)
        for i, j in zip(v1, v2):
            ix = int(i)
            jx = int(j)
            if ix > jx:
                return 1
            elif ix < jx:
                return -1
            else:
                continue
        return 0


print(Solution().compareVersion(version1="1.01", version2="1.001"))

from functools import reduce

print(reduce(lambda x, y: x * y, [1, 2, 3, 4, 5, 6, 7, 8, 9]))
