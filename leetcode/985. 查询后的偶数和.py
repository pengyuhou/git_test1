class Solution(object):
    def sumEvenAfterQueries(self, A, queries):
        ret = []

        for i in range(len(queries)):
            tmp=A[queries[i][1]]
            A[queries[i][1]] += queries[i][0]

            if i==0:
                res=sum([x for x in A if not x%2])
                ret.append(res)
            else:
                if A[queries[i][1]]%2 != 0 and tmp%2 != 0:
                    ret.append(res)
                elif A[queries[i][1]]%2 != 0 and tmp%2==0:
                    res-=tmp
                    ret.append(res)
                elif A[queries[i][1]]%2 == 0 and tmp%2==0:
                    res -= tmp
                    res += A[queries[i][1]]
                    ret.append(res)
                elif A[queries[i][1]]%2 == 0 and tmp%2 !=0:
                    res += A[queries[i][1]]
                    ret.append(res)
        return ret


if __name__ == "__main__":
    A=[3, 2]
    queries=[[4, 0], [3, 0]]
    A = [1, 2, 3, 4]
    queries = [[1, 0], [-3, 1], [-4, 0], [2, 3]]
    print(Solution().sumEvenAfterQueries(A,queries))







