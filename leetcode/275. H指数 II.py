class Solution(object):
    def hIndex(self, citations):
        if citations == []:
            return 0
        citations = citations[::-1]
        max_val = -float('inf')
        for i in range(len(citations)):
            if i + 1 >= citations[i]:
                max_val = max(max_val,citations[i])
            else:
                max_val = max(max_val,i+1)
        return max_val

if __name__ == "__main__":
    print(Solution().hIndex([0, 1, 3, 5, 6]))
