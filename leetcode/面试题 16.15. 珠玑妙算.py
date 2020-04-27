class Solution(object):
    def masterMind(self, solution, guess):
        a = {}
        b = {}
        for i in solution:
            if i not in a.keys():
                a[i] = 1
            else:
                a[i] += 1
        for i in guess:
            if i not in b.keys():
                b[i] = 1
            else:
                b[i] += 1
        R_num = min(a['R'], b['R']) if 'R' in a.keys() and 'R' in b.keys() else 0
        G_num = min(a['G'], b['G']) if 'G' in a.keys() and 'G' in b.keys() else 0
        B_num = min(a['B'], b['B']) if 'B' in a.keys() and 'B' in b.keys() else 0
        Y_num = min(a['Y'], b['Y']) if 'Y' in a.keys() and 'Y' in b.keys() else 0
        a = R_num + G_num + B_num + Y_num
        count = 0
        for i, j in zip(solution, guess):
            if i == j:
                count += 1
        return [count,a-count]
    
if __name__ == "__main__":
    solution = "RGBY"
    guess = "GGRR"
    print(Solution().masterMind(solution,guess))










