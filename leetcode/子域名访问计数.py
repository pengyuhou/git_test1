class Solution:
    def subdomainVisits(self, cpdomains):
        ret = []
        for i in range(len(cpdomains)):
            a = []
            res = cpdomains[i].split(' ')
            count = int(res[0])
            a.append(count)
            a.append(res[1])
            a.append(res[1].split('.', 1)[-1])
            if res[1].count('.') > 1:
                a.append(res[1].split('.', 2)[-1])
            ret.append(a)
        a = {}
        for i in range(len(ret)):
            for j in ret[i][1:]:
                if j not in a.keys():
                    a[j] = ret[i][0]
                else:
                    a[j] += ret[i][0]
        ret = [str(v) + ' ' + k for k, v in a.items()]
        return ret

if __name__ =="__main__":
    cpdomains=["9001 discuss.leetcode.com"]
    print(Solution().subdomainVisits(cpdomains))


















