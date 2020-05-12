class Solution(object):
    def diffWaysToCompute(self, s):
        if '+' not in s and '-' not in s and '*' not in s:
            return [int(s)]
        s = list(s)
        tmp = s
        s = list(enumerate(s))
        ret = []
        for i, j in s:
            if j == '+' or j == '-' or j == "*":
                left = self.diffWaysToCompute(''.join(tmp[:i]))
                right = self.diffWaysToCompute(''.join(tmp[i + 1:]))
                for x in left:
                    for y in right:
                        if j == '+':
                            ret.append(x + y)
                        elif j == '-':
                            ret.append(x - y)
                        else:
                            ret.append(x * y)
        return ret


if __name__ == "__main__":
    print(Solution().diffWaysToCompute("11"))
