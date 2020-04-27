class Solution:
    def removeDuplicates(self, S: str) -> str:
        stack = []

        for i in s:
            if stack == []:
                stack.append(i)

            else:
                if stack[-1] == i:
                    stack.pop()
                else:
                    stack.append(i)
        return ''.join(stack)





if __name__ == '__main__':
    s  = "abbaca"
    ss=Solution()
    print(ss.removeDuplicates(s))




































