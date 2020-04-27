class Solution(object):
    def balancedStringSplit(self, s):

        s = list(s)
        sum_r = 0
        sum_l = 0
        ret = 0
        for i in s:
            if i == 'R':
                sum_r += 1
            if i == 'L':
                sum_l -= 1
            if sum_r + sum_l == 0:
                ret += 1
        return ret


if __name__ == '__main__':
    pass











