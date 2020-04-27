class Solution:

    def reverseBits(self, n):
        a=list(str(bin(n)))

        l = 34 - len(a)
        while l > 0:
            a.insert(2, str(0))
            l -= 1
        t = a[2:]
        t.reverse()
        res = a[:2] + t
        ret = "".join(res)
        print(ret)
        index = len(ret) - 1
        sum1 = 0
        count = 0
        for i in range(index, 2, -1):
            sum1 += int(ret[i]) * pow(2, count)
            count += 1
        return bin(sum1)



if __name__ == '__main__':
    a = 0b00000010100101000001111010011100
    S=Solution()
    print(S.reverseBits(a))























