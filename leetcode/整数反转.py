x=1534236469
x1=2**31+1
print(x1)

class Solution(object):
    def reverse(self, x):
        if x<2**31-1 and x>(-2)**31:
            if x<0:
                x=-x
                x = str(x)
                x = list(x)
                x.reverse()
                x = "".join(x)
                ret="-"+x
                return int(ret)
            else:
                x=str(x)
                x=list(x)
                x.reverse()
                x="".join(x)
                return int(x)
        else:
            return 0
s=Solution()
print((s.reverse(x)))



