class Solution(object):
    def fun(self, a, b):
        count = 0
        for i, j in zip(a, b):
            if i != j:
                count += 1
        if count == 1:
            return True
        else:
            return False

    def minMutation(self, start, end, bank):
        queue = [start]
        mark = [False for _ in range(len(bank))]
        if start in bank:
            mark[bank.index(start)] = True
        count = 1
        while queue:
            for _ in range(len(queue)):
                a = queue.pop(0)
                for i in range(len(bank)):
                    if self.fun(a, bank[i]) and bank[i] == end:
                        return count
                    if self.fun(a, bank[i]) and not mark[i]:
                        mark[i] = True
                        queue.append(bank[i])
            count += 1
        return -1



if __name__ == "__main__":
    print(Solution().minMutation(start="AACCGGTT",
                                 end="AAACGGTA",
                                 bank=["AACCGGTA", "AACCGCTA", "AAACGGTA"]))
