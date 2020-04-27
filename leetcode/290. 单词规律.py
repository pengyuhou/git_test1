class Solution(object):
    def wordPattern(self, pattern, str):
        res = str.split()
        p = list(pattern)
        a = {}
        index = 0
        if len(p)==len(res):
            for i in res:
                if p[index] not in a.keys() and i not in a.values():
                    a[p[index]] = i
                    index += 1
                elif p[index] not in a.keys() and i in a.values():
                    return False
                else:
                    if i != a[p[index]]:
                        return False
                    else:
                        index += 1
            return True
        else:
            return False

if __name__ == "__main__":
    pattern = "aaa"
    str = "aa aa aa aa"
    # str = "dog dog dog dog"
    print(Solution().wordPattern(pattern,str))






