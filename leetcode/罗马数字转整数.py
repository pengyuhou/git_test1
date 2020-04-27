class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        a = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000,
            'IV': 4,
            'IX': 9,
            'XL': 40,
            'XC': 90,
            'CD': 400,
            'CM': 900
        }
        index = len(s) - 1
        ret = 0
        while index >= 0:
            if index:
                now = s[index]
                nex = s[index - 1]
                if (now == 'V' and nex == 'I') or (now == 'X' and nex == 'I') or (now == 'L' and nex == 'X') or (
                        now == 'C' and nex == 'X') or (now == 'D' and nex == 'C') or (now == 'M' and nex == 'C'):
                    c = nex + now
                    ret += a.get(c)
                    index -= 2

                else:
                    ret += a.get(now)
                    index -= 1
            else:
                ret += a.get(s[index])
                index -= 1
        return ret

if __name__ == '__main__':
    s = 'MCMXCIV'
    q=Solution()
    print(q.romanToInt(s))








