class Solution(object):
    def complexNumberMultiply(self, a, b):
        a_ = a.split('+')
        b_ = b.split('+')
        x1 = a_[0]
        y1 = a_[1].replace('i', '')
        x2 = b_[0]
        y2 = b_[1].replace('i', '')
        real = int(x1) * int(x2) - int(y1) * int(y2)
        ima = int(y1) * int(x2) + int(x1) * int(y2)
        return str(real) + '+' + str(ima) + 'i'



if __name__ == "__main__":
    a = "1+-1i"
    b = "1+-1i"
    print(Solution().complexNumberMultiply(a,b))

