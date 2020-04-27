import re
class Solution(object):
    def defangIPaddr(self, address):
        """
        :type address: str
        :rtype: str
        """
        return address.replace('.', '[.]')


if __name__ == '__main__':
    address = "255.100.50.0"
    # print(address.replace('.', '[.]'))
    # s=Solution()
    # print(s.defangIPaddr(address))
    # pattern=re.compile('\d+(.)\d+(.)\d+(.)\d')
    # print(re.sub(pattern ,address))


