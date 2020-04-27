class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        l1 = len(str1)
        l2 = len(str2)
        str1 = list(str1)
        str2 = list(str2)
        index = 0
        ret = []
        while index<l1 and index<l2:
            if str1[index] == str2[index]:
                ret.append(str1[index])
            index += 1
        if ret==[]:
            return ''
        while True:
            if l1%len(ret)==0 and l2%len(ret)==0 and set(ret) ==set(str1) and set(ret)==set(str2):
                return ''.join(ret)
            ret = ret[:-1]
            if len(ret)==0:
                return ''




if __name__ == "__main__":
    str1 = "ABCDEF"
    str2 = "ABC"
    # print()
    print(Solution().gcdOfStrings(str1,str2))


