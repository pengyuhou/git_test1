class Solution(object):
    def firstUniqChar(self, s):
        index1 = -1
        for i in s:
            index1 += 1
            flag = True
            index2 = -1
            for j in s.replace(i, '', 1):
                index2 += 1
                if i == j:
                    flag = not flag
                    break
            if flag:
                return index1
        return -1

if __name__ == '__main__':
    s = "loeleeoev"
    # s = 'llle'

    s1=Solution()
    print(s1.firstUniqChar(s))
