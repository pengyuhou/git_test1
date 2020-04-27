class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        stack = []
        s = list(s)
        for i in range(len(s)):
            if not stack:
                stack.append([s[i], 1])
            else:
                tmp = s[i]
                if tmp == stack[-1][0]:
                    x = stack[-1][1] + 1
                    if x<k:
                        stack.append([tmp,x])
                    else:
                        stack = stack[:-(k-1)]
                else:
                    stack.append([tmp,1])
        return ''.join([i for i,j in stack])


if __name__ == "__main__":
    s = "deeedbbcccbdaa"
    k = 3
    print(Solution().removeDuplicates(s, k))
