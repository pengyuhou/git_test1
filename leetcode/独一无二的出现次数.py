class Solution:
    def uniqueOccurrences(self, arr) :
        a = {}
        for i in arr:
            if i not in a.keys():
                a[i] = 1
            else:
                a[i] += 1
        x=list(a.values())


        return len(set(x))==len(x)

if __name__ == '__main__':
    arr = [-3, 0, 1, -3, 1, 1, 1, -3, 10, 0]

    print(Solution().uniqueOccurrences(arr))


    # print(a.keys())
    # print(a.values())




