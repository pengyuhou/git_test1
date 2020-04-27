class Solution(object):
    def frequencySort(self, s):
        s = list(s)
        a = {}
        for i in s:
            if i not in a.keys():
                a[i] = 1
            else:
                a[i] += 1
        res=sorted(a.items(),key=lambda x:x[1],reverse=True)
        ret = ''
        for i,j in res:
            ret += i*j
        return ret

print(Solution().frequencySort("Aabb"))