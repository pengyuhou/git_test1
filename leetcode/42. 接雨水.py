class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        if height==[]:
            return 0
        max_index = height.index(max(height))
        a = height[:max_index + 1]
        b = height[max_index:]
        b.reverse()
        # index = 0
        # while a[index] == 0:
        #     a.pop(0)
        def fun(a):
            stack = []
            count_f = 0
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
                    count_f += tmp
                    stack.clear()
                    stack.append(a[i])
            return count_f

        return fun(a)+fun(b)




if __name__ == "__main__":
    print(Solution().trap([0,1,0,2,1,0,1,3,2,1,2,1,100,0,0,99,3,5,6,7,1]))
