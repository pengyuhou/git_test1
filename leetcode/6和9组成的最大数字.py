class Solution(object):
    def maximum69Number (self, num):
        """
        :type num: int
        :rtype: int
        """
        num = list(str(num))
        for i in range(len(num)):
            if num[i] == '6':
                num[i] = '9'
                break
        return int(''.join(num))


if __name__ =='__main__':
    num = 9996
    num=list(str(num))
    for i in range(len(num)):
        if num[i]=='6':
            num[i]='9'
            break
    print(int(''.join(num)))

