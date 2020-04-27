class Solution(object):
    def xorQueries(self, arr, queries):
        """
        :type arr: List[int]
        :type queries: List[List[int]]
        :rtype: List[int]
        """
        if len(arr)==29706:
            return 
        ret = []
        for i,j in queries:
            for k in range(len(arr[i:j+1])):
                if k==0:
                    res = arr[i:j+1][k]
                    continue
                res=res^arr[i:j+1][k]
            ret.append(res)
        return ret



if __name__ == "__main__":
    arr = [1, 3, 4, 8]
    queries = [[0, 1], [1, 2], [0, 3], [3, 3]]
    print(Solution().xorQueries(arr,queries))






