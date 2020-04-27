class Solution1(object):
    def fraction(self, cont):

        l = len(cont)
        index = l-1
        if l==1:
            return [cont[0],1]
        ret = [None,None]
        while index>=0:
            if index==l-1:
                ret[0] = 1
                ret[1] = cont[index]
                index -= 1
            tmp = ret[0]
            ret[0] = ret[1]
            ret[1] = tmp + cont[index]*ret[1]
            index -= 1
        ret.reverse()
        return ret


if __name__ == "__main__":
    cont = [3, 2, 0, 2]
    # cont = [0, 0, 3]
    # cont = [5, 1, 0, 6, 1, 7, 2, 6, 6, 4]
    cont = [2147483647]

    print(Solution1().fraction(cont))



