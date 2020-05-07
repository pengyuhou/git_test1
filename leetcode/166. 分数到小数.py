class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        res = numerator/denominator
        ox,b = str(res).split('.')
        tmp_b = b
        if b=='0':
            return str(ox)
        shengyu = 0
        count = []
        for _ in range(len(b)):
            a = {}
            ret = []
            for node in list(b):
                if node not in a.keys():
                    a[node] = 1
                else:
                    a[node] += 1
                x = list(a.values())
                ret.append(x)
                for i in range(len(ret)-1):
                    tmp = []
                    for j in range(len(ret[i])):
                        tmp.append(ret[i][j]*2)
                    if tmp==x:
                        count.append(sum(ret[i]))
            if count:
                break
            b = b[1:]
            shengyu += 1
        if count:
            res = ox +'.'+b[:min(count)]
            while res[-1]=='0':
                res = res[:-1]
            a,b = res.split('.')
            return a+'.'+tmp_b[:shengyu]+'({})'.format(b)

        else:

            return ox+'.'+tmp_b




if __name__ == "__main__":
    print(Solution().fractionToDecimal( numerator = 258, denominator = 4545))

















