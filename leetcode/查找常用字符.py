class Solution(object):
    def commonChars(self, A):
        """
        :type A: List[str]
        :rtype: List[str]
        """
        ret = []
        for i in A[0]:
            index = 0
            for j in range(1, len(A)):
                if i in A[j]:
                    index += 1
            if index == len(A) - 1:
                ret.append(i)
                for k in range(1, len(A)):
                    A[k] = A[k].replace(i, '', 1)

        return ret


if __name__ == '__main__':
    A = ["bella","label","roller"]
    A=["cool","lock","cook"]
    A=["acabcddd","bcbdbcbd","baddbadb","cbdddcac","aacbcccd","ccccddda","cababaab","addcaccd"]




















