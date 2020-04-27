class Solution(object):
    def maxDepthAfterSplit(self, seq):
        """
        :type seq: str
        :rtype: List[int]
        """

        ans = []
        index = 0
        for s in seq:
            if s == '(':
                index += 1
                ans.append(index % 2)
            else:
                ans.append(index % 2)
                index -= 1
        return ans


if __name__ == "__main__":
    print(Solution().maxDepthAfterSplit("(()())"))
