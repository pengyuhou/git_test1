class Solution(object):
    def groupAnagrams(self, strs):
        a = {}
        for s in strs:
            ret = sorted(s)
            res = ''.join(ret)
            if res not in a.keys():
                a[res] = [s]
            else:
                a[res].append(s)
        ret = [i for i in a.values()]
        return ret


if __name__ == "__main__":
    print(Solution().groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))
