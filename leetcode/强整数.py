class Solution:
    def powerfulIntegers(self, x: int, y: int, bound):
        ret = []
        i, j = 0, 0
        if x==1 and y ==1 and bound >=2:
            return [2]
        elif x==1 and y ==1 and bound <2:
            return []
        if x==1 and y!=1:
            while 1+y**j<=bound:
                ret.append(1+y**j)
                j += 1
        if x!=1 and y==1:
            while x**i+1<=bound:
                ret.append(1+x**i)
                i += 1
        while x ** i + y ** j <= bound:
            while x ** i + y ** j <= bound:
                c = x ** i + y ** j

                ret.append(c)
                j += 1
            j = 0
            i += 1
        res = list(set(ret))
        return res



if __name__ =="__main__":
    x = 1
    y = 1
    bound = 1
    # x = 2
    # y = 1
    # bound = 10

    print(Solution().powerfulIntegers(x,y,bound))




