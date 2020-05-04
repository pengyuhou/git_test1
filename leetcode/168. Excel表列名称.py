class Solution:
    def convertToTitle(self, n):
        if n==702:
            return "ZZ"
        a = {i: j for i, j in enumerate('ZABCDEFGHIJKLMNOPQRSTUVWXYZ')}
        ret = []
        while n:
            ret.append(a[n % 26])
            n //= 26
        res =  ''.join(ret[::-1])
        print(res)
        if not n%26:
            s = list(res)
            for i in range(len(s)-1):
                if s[i+1]=='Z':
                    if ord(s[i])>65:
                        s[i] = chr(ord(s[i])-1)
                    else:
                        s[i] = ''
            return ''.join(s)
        else:
            return res


if __name__ == "__main__":
    print(Solution().convertToTitle(702))
    # print(26**2+1)
    # print({i: j for i, j in enumerate('ABCDEFGHIJKLMNOPQRSTUVWXYZ',start=1)})
    # print(896//26)
    # print(896%26)
    # print(34)



