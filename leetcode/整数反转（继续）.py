class Solution(object):
    def reverse(self, x):

        x1 = -2147483648
        x2 = 2147483647

        if x == 0:
            return 0
        else:
            if x > 0:
                a = list(str(x))
                a.reverse()

                while '0' in a[0]:
                    a.remove('0')
                a= int(''.join(a))
                if a<x2 and a>x1:
                    return a
                else:
                    return 0

            else:
                a = list(str(x)[1:])
                a.reverse()
                a.insert(0, '-')
                while '0' in a[1]:
                    a.remove('0')
                a= int(''.join(a))
                if a<x2 and a>x1:
                    return a
                else:
                    return 0

if __name__ == "__main__":


    x=1534236469
    print(Solution().reverse(x))




