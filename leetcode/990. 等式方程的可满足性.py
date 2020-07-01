class Solution(object):
    def equationsPossible(self, equations):
        def find(x):
            if x == p[x]:
                return p[x]
            else:
                p[x] = find(p[x])
                return p[x]

        p = [i for i in range(26)]
        for i in equations:
            if i[1] == '=':
                r1 = find(ord(i[0]) - ord('a'))
                r2 = find(ord(i[3]) - ord('a'))
                if r1 != r2:
                    p[r2] = r1
        print(p)
        for i in equations:
            if i[1] == '!':
                r1 = find(ord(i[0]) - ord('a'))
                r2 = find(ord(i[3]) - ord('a'))
                if r1 == r2:
                    return False
        return True


print(Solution().equationsPossible(["a==b", 'a!=c', 'b==d']))
