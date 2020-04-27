class Solution(object):
    def isFlipedString(self, s1, s2):
        if s1=='' and s2=='':
            return True
        if len(s1) == len(s2) and len(set(s1)) == len(set(s2)):
            s1 = list(s1)
            s2 = list(s2)
            for i in range(len(s2)):
                x = s2.pop()
                s2.insert(0, x)
                if s1 == s2:
                    return True
            return False
        else:
            return False

if  __name__ == "__main__":

    s1 = "A"
    s2 = "A"
    print(Solution().isFlipedString(s1,s2))










