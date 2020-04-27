class Solution(object):
    def checkRecord(self, s):
        a = list(s)
        if a.count('A')>1:
            return False
        else:
            for i in range(len(a)):
                if i+2 <= len(a)-1:
                    if a[i]=='L' and a[i+1]=='L' and a[i+2]=='L':
                        return False
            return True

if __name__ =="__main__":
    s="APLLPPLPPLLL"
    print(Solution().checkRecord(s))






