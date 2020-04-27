class Solution(object):
    def addBinary(self, a, b):
        sum0 = 0
        index0 = 0
        sum1 = 0
        index1 = 0
        if a=='0' and b=='0':
            return '0'

        for i in a:
            i = int(i)
            sum0 += i * pow(2, len(a)-index0-1)
            index0 += 1
        for j in b:
            j = int(j)
            sum1 += j * pow(2,len(b)- index1-1)
            index1 += 1
        sum_total = sum0 + sum1
        a1 = []
        while sum_total:
            res = sum_total % 2
            sum_total = sum_total // 2
            res = str(res)
            a1.append(res)
        a1.reverse()
        return ''.join(a1)


if __name__ == "__main__":
    a='0'
    b='0'
    s=Solution()
    print(s.addBinary(a, b))





























