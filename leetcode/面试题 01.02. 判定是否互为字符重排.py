class Solution(object):
    def CheckPermutation(self, s1, s2):
        return sorted(list(set(s1)))==sorted(list(set(s2)))



if __name__ == "__main__":
    s1 = "abc"
    s2 = "bad"
    print(Solution().CheckPermutation(s1,s2))
    # a=sorted(list(set(s1)))
    # b = sorted(list(set(s2)))


    # print(a==b)





