class Solution(object):
    def thirdMax(self, nums):
        a=nums
        stack = []
        for i in range(len(a)):
            if a[i] in stack:
                continue
            if len(stack) == 0:
                stack.append(a[i])
            elif len(stack) == 1:
                if a[i] > stack[0]:
                    stack.insert(0, a[i])
                else:
                    stack.append(a[i])
            elif len(stack) == 2:
                if a[i] > stack[0]:
                    stack.insert(0, a[i])
                elif a[i] > stack[1]:
                    stack.insert(1, a[i])
                else:
                    stack.append(a[i])
            elif len(stack) >= 3:
                if a[i] > stack[0]:
                    stack.insert(0, a[i])
                elif a[i] > stack[1]:
                    stack.insert(1, a[i])
                elif a[i] > stack[2]:
                    stack.insert(2, a[i])
                else:
                    stack.append(a[i])
        if len(stack)>=3 :
            return stack[2]
        else:
            return stack[0]



if __name__ == '__main__':
    a= [2, 2, 3, 1]
    print(Solution().thirdMax(a))




















