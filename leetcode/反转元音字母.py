class Solution(object):
    def reverseVowels(self, s):
        s = list(s)
        l_s = len(s)
        index1 = 0
        index2 = l_s - 1
        flag1 = False
        flag2 = False
        while index2 > index1:
            if s[index1] is 'A' or s[index1] is 'E' or s[index1] is 'I' or s[index1] is 'O' or s[index1] is 'U' or s[
                index1] is 'a' or s[index1] is 'e' or s[index1] is 'i' or s[index1] is 'o' or s[index1] is 'u':
                flag1 = True
            else:
                flag1 = False
            if s[index2] is 'A' or s[index2] is 'E' or s[index2] is 'I' or s[index2] is 'O' or s[index2] is 'U' or s[
                index2] is 'a' or s[index2] is 'e' or s[index2] is 'i' or s[index2] is 'o' or s[index2] is 'u':
                flag2 = True
            else:
                flag2 = False
            if flag1 and flag2:
                s[index1], s[index2] = s[index2], s[index1]
                index1 += 1
                index2 -= 1
            if flag1 and not flag2:
                index2 -= 1
            if not flag1 and flag2:
                index1 += 1
            if not flag1 and not flag2:
                index1 += 1
                index2 -= 1
        return "".join(s)


if __name__ == '__main__':
    s="hello"
    S1=Solution()
    print(S1.reverseVowels(s))












