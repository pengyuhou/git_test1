class Solution:
    def compress(self, chars) :
        a = {}
        for i in range(len(chars)):
            if chars[i] not in a.keys():
                a[chars[i]] = 1
            else:
                a[chars[i]] += 1
        a = [[i, j] for i, j in a.items()]
        ret = []
        for x in a:
            ret.append(x[0])
            if x[1] <= 9 and x[1] >= 2:
                ret.append(str(x[1]))
            if x[1] >= 10:
                t = list(str(x[1]))
                for i in t:
                    ret.append(i)
        return ret


if __name__ == "__main__":
    chars=["a","a","b","b","c","c","c"]
    print(Solution().compress(chars))













