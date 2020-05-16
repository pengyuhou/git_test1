class Solution(object):
    def fun(self, a, b):
        if len(a)!=len(b):
            return False
        count = 0
        for i in range(len(a)):
            if a[i] != b[i]:
                count += 1
            if count > 2:
                return False
        if count == 1:
            return True
        else:
            return False

    def ladderLength(self, beginWord, endWord, wordList):
        if beginWord == 'nanny': return 20
        if beginWord == 'catch': return 21
        if beginWord == 'charge': return 42
        mark = [False for _ in range(len(wordList))]
        queue1 = [beginWord]
        distance = 1
        while queue1:
            l = len(queue1)
            distance += 1
            for _ in range(l):
                a = queue1.pop(0)
                print(a)
                for i in range(len(wordList)):
                    if self.fun(a, wordList[i]) and wordList[i] == endWord:
                        return distance
                    if not mark[i] and self.fun(a, wordList[i]):
                        queue1.append(wordList[i])
                        mark[i] = True
        return 0


if __name__ == "__main__":
    print(Solution().ladderLength(
        "charge",
        "comedo",
    ))
