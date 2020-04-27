class Solution(object):
    def toGoatLatin(self, S):
        """
        :type S: str
        :rtype: str
        """
        a = S.split(' ')
        index = 0
        ret = []
        for i in a:
            if i != ' ':
                index += 1
            if i[0] == 'a' or i[0] == 'e' or i[0] == 'i' or i[0] == 'o' or i[0] == 'u' or i[0] == 'A' or i[0] == 'E' or \
                            i[0] == 'I' or i[0] == 'O' or i[0] == 'U':
                i += 'ma'
                i += 'a' * index
                ret.append(i)
            if not (i[0] == 'a' or i[0] == 'e' or i[0] == 'i' or i[0] == 'o' or i[0] == 'u' or i[0] == 'A' or i[
                0] == 'E' or i[0] == 'I' or i[0] == 'O' or i[0] == 'U'):
                i += i[0]
                i = i[1:]
                i += 'ma'
                i += 'a' * index
                ret.append(i)
        return " ".join(ret)

if __name__ == '__main__':
    S="I speak Goat Latin"
    s=Solution()
    print(s.toGoatLatin(S))











