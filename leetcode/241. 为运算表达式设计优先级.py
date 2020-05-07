"""
分治思想
"""
class Solution(object):
    def diffWaysToCompute(self, s):
        """
        :type input: str
        :rtype: List[int]
        """
        if s.isdigit():
            return [int(s)]
        ret = []
        for i, char in enumerate(s):
            if char in ['+', '-', '*']:
                left = self.diffWaysToCompute(s[:i])
                right = self.diffWaysToCompute(s[i + 1:])
                for l in left:
                    for r in right:
                        if char=='+':
                            ret.append(l+r)
                        elif char=='-':
                            ret.append(l-r)
                        else:
                            ret.append(l*r)
        return ret


if __name__ == "__main__":
    # print(Solution1().diffWaysToCompute("2-1-1"))
    print(Solution().diffWaysToCompute("2-1-1"))
