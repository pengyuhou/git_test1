class Solution(object):
    def countSegments(self, s):
        sum = 0
        i = 0
        flag = False
        while i <= len(s) - 1:
            while (ord(s[i]) >= ord('A') and ord(s[i]) <= ord('Z')) or (
                    ord(s[i]) >= ord('a') and ord(s[i]) <= ord('z')) or ord(s[i])==ord("'") or ord(s[i])==ord('-'):
                i += 1
                if i == len(s):
                    flag = True
                    break
                flag = True

            if flag:
                sum += 1

            if i == len(s):
                break
            while ord(s[i]) == ord(' ') or ord(s[i]) == ord(',') or ord(s[i]) ==ord('!') or ord(s[i]) == ord("'") or ord(s[i])==ord('.'):


                i += 1
                if i == len(s):
                    flag = False
                    break
                flag = False
        return sum

if __name__ == '__main__':
    # s1="Hello my name is John"
    # s1="The one-hour drama series Westworld is a dark odyssey about the dawn of artificial consciousness and the evolution of sin. Set at the intersection of the near future and the reimagined past, it explores a world in which every human appetite, no matter how noble or depraved, can be indulged."
    s1=''
    # s="                "
    # s='               '
    # s='DADa '
    # print(ord('A'),ord('Z'),ord('a'),ord('z'))
    # print(ord(' '),ord(','))
    # sum=0
    # i=0
    # flag =False
    # while i<=len(s)-1:
    #     while (ord(s[i])>=ord('A') and ord(s[i])<=ord('Z')) or (ord(s[i])>=ord('a') and ord(s[i])<=ord('z')):
    #         i += 1
    #         if i==len(s):
    #             flag =True
    #             break
    #         flag = True
    #
    #     if flag:
    #         sum += 1
    #
    #     if i == len(s):
    #         break
    #     while ord(s[i])==ord(' ') or ord(s[i]) == ord(','):
    #         i += 1
    #         if i==len(s):
    #             flag = False
    #             break
    #         flag = False
    #
    # print(sum)
    # print(ord("'"))


    s=Solution()
    print(s.countSegments(s1))





















