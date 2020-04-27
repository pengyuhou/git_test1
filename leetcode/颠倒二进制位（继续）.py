class Solution:
    def reverseBits(self, n: int) -> int:
        a = list(bin(n))
        a = a[2:]

        while len(a) < 32:
            a.insert(0, '0')
        a = a[::-1]
        x = ''.join(a)
        a = (int(x, base=2))
        return a


if __name__ == "__main__":
    n=0b00000010100101000001111010011100
    print(Solution().reverseBits(n))









