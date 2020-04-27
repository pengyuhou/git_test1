class Solution(object):
    def twoCitySchedCost(self, costs):
        """
        :type costs: List[List[int]]
        :rtype: int
        """
        a=costs
        b = sorted(a, key=lambda x: x[0] - x[1])
        sum = 0
        l=len(b)
        for i in range(l // 2):
            sum += b[i][0]
        for j in range(l// 2, l):
            sum += b[j][1]
        return sum


if __name__ == "__main__":
    a=[[10, 20], [30, 200], [400, 50], [30, 20]]

    print(sum)












