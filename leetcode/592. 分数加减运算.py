class Solution:
    def fractionAddition(self, expression: str) -> str:
        def gdc(p, q):
            p = abs(p)
            q = abs(q)
            if q == 0:
                return p
            if p < q:
                p, q = q, p
            r = p % q
            return gdc(q, r)
        sym = []
        num = []
        den = []
        for i in range(len(expression)):
            if expression[i] == '/':
                index = i - 1
                index1 = i + 1
                tmp = []
                while index >= 0 and expression[index].isdigit():
                    tmp.append(expression[index])
                    index -= 1
                num.append(''.join(tmp[::-1]))
                if index >= 0:
                    sym.append(expression[index])
                else:
                    sym.append('+')
                tmp.clear()
                while index1 < len(expression) and expression[index1].isdigit():
                    tmp.append(expression[index1])
                    index1 += 1
                den.append(''.join(tmp))
        den = list(map(int, den))
        num = list(map(int, num))
        from functools import reduce
        val_den = reduce(lambda x, y: x * y, den)
        val_num = [i * (val_den // j) for i, j in zip(num, den)]
        res = 0
        for i in range(len(sym)):
            if sym[i] == '+':
                res += val_num[i]
            else:
                res -= val_num[i]
        if res == 0:
            return "0/1"
        x = gdc(res, val_den)
        ret = f"{res // x}/{val_den // x}"
        q = ret.index('/')
        if ret[q + 1] == '-':
            if ret[0] == '-':
                return ret[1:q+1]+ret[q+2:]
            else:
                return '-'+ret[:q+1]+ret[q+2:]
        return ret


if __name__ == "__main__":
    print(Solution().fractionAddition("-5/2+10/3+7/9"))
