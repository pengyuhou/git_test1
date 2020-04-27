class Solution(object):
    def checkPerfectNumber(self, num):
        if num ==1:
            return False
        if num <= 0:
            return False
        n=num
        if not n % n**0.5:
            a =int(n**0.5)
        else:
            a=int(n**0.5)+1
        ret = [1,]
        for i in range(2,a):
            if not num%i:
                ret.append(i)
                ret.append(num//i)
        return sum(ret)==num


if __name__ == "__main__":
    n = 0
    print(Solution().checkPerfectNumber(n))









