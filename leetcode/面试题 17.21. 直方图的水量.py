class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        if height==[]:
            return 0
        mark = height.index(max(height))
        a = height[:mark + 1]
        b = height[mark:]
        b.reverse()
        def fun(a):
            stack = []
            count = 0
            for i in range(len(a)):
                if stack == []:
                    stack.append(a[i])
                    continue
                if a[i] < stack[0]:
                    stack.append(a[i])
                    continue
                if a[i] >= stack[0]:
                    tmp = 0
                    for j in range(1, len(stack)):
                        tmp += stack[0] - stack[j]
                    count += tmp
                    stack.clear()
                    stack.append(a[i])
            return count

        return fun(a)+fun(b)


if __name__ == "__main__":
    print(Solution().trap([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]))
