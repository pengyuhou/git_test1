class Solution(object):
    def canPermutePalindrome(self, s):
        a=set(s)
        ret=[]
        for i in a:
            ret.append(s.count(i))
        count=0
        for i in ret:
            if i%2==1:
                count +=1
            if count >=2:
                return False
        else:
            return True


if __name__ == "__main__":

    s="aabbccdf"
    print(Solution().canPermutePalindrome(s))


