class Solution:
    def intToRoman(self, num: int) -> str:
        a = {1: 'I', 4: 'IV', 5: 'V', 9: 'IX', 10: 'X', 40: 'XL', 50: 'L', 90: 'XC', 100: 'C', 400: 'CD', 500: 'D',
             900: 'CM', 1000: 'M'}
        bt = {1: 'I', 5: 'V', 10: 'X', 50: 'L', 100: 'C', 500: 'D', 1000: 'M'}
        bits = []
        while num:
            bits.append(num % 10)
            num //= 10
        bits.reverse()
        index = len(bits) - 1
        res = ''
        for bit in bits:
            if not bit:
                index -= 1
                continue
            num_real = bit * 10 ** index

            if num_real not in a.keys():
                b = list(bt.items())
                b.reverse()
                for i, j in b:
                    while num_real:
                        ret1 = num_real // i
                        if not ret1:
                            break
                        res += j * ret1
                        num_real -= ret1 * i
            else:
                res += a[num_real]
            index -= 1
        return res


if __name__ == "__main__":
    print(Solution().intToRoman(201))
