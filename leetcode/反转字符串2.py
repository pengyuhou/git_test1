class Solution(object):
    def reverseStr(self, s, k):
        a = list(s)
        l = len(a)
        left1 = 0
        right1 = k
        left2 = k
        k2=2*k
        right2 = k2
        if l % k2:
            n = l // k2 + 1
        else:
            n = l // k2
        ret = []
        for i in range(n):
            x = a[left1:right1]
            x.reverse()
            ret += x
            t = a[left2:right2]
            ret += t
            left1 += k2
            right1 += k2
            left2 += k2
            right2 += k2
        return ''.join(ret)

if __name__ == "__main__":
    s = "abcdefg"
    k = 2
    print(Solution().reverseStr(s,k))












