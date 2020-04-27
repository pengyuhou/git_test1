class Solution(object):
    def uncommonFromSentences(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: List[str]
        """
        a = A
        b = B
        a = a.split(' ')
        b = b.split(' ')

        a_count = {}
        b_count = {}
        for i in a:
            if i not in a_count.keys():
                a_count[i] = 1
            else:
                a_count[i] += 1

        for i in b:
            if i not in b_count.keys():
                b_count[i] = 1
            else:
                b_count[i] += 1

        ret = []
        for key, value in a_count.items():
            if value == 1 and key not in b:
                ret.append(key)
        for key, value in b_count.items():
            if value == 1 and key not in a:
                ret.append(key)

        return ret


if __name__ == '__main__':
    A="abcd def abcd xyz"
    B="ijk def ijk"
    print(Solution().uncommonFromSentences(A,B))

     










