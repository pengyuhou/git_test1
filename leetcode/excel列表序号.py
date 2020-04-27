class Solution(object):
    def titleToNumber(self, s):
        d={'A':1,
           'B':2,
           'C':3,
           'D':4,
           'E':5,
           'F':6,
           'G':7,
           'H':8,
           'I':9,
           'J':10,
           'K':11,
           'L':12,
           'M':13,
           'N':14,
           'O':15,
           'P':16,
           'Q':17,
           'R':18,
           'S':19,
           'T':20,
           'U':21,
           'V':22,
           'W':23,
           'X':24,
           'Y':25,
           'Z':26
        }



        cur=len(s)-1
        sum=0
        for i in range(len(s)):
            a=(d[s[cur]])
            sum += a*pow(26,i)

            cur -= 1

        return sum

if __name__ == '__main__':
    s=Solution()
    print(s.titleToNumber('ZY'))

    # d={'A':1,
    #    'B':2,
    #    'C':3,
    #    'D':4,
    #    'E':5,
    #    'F':6,
    #    'G':7,
    #    'H':8,
    #    'I':9,
    #    'J':10,
    #    'K':11,
    #    'L':12,
    #    'M':13,
    #    'N':14,
    #    'O':15,
    #    'P':16,
    #    'Q':17,
    #    'R':18,
    #    'S':19,
    #    'T':20,
    #    'U':21,
    #    'V':22,
    #    'W':23,
    #    'X':24,
    #    'Y':25,
    #    'Z':26
    # }
    #
    #
    # s='ZY'
    # cur=len(s)-1
    # sum=0
    # for i in range(len(s)):
    #     a=(d[s[cur]])
    #     sum += a*pow(26,i)
    #
    #     cur -= 1
    #
    # print(sum)
