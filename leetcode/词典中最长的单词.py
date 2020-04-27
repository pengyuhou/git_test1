class Solution(object):
    def longestWord(self, words):
        words = sorted(list(set(words)))
        a = {}
        for word in words:
            if word[0] not in a.keys() and len(word) == 1:
                a[word[0]] = [word]
            elif word[0] in a.keys():
                if len(word) - len(a[word[0]][0]) == 1:
                    for x in a[word[0]]:
                        if x in word:
                            a[word[0]].clear()
                            a[word[0]].append(word)
                elif len(word) == len(a[word[0]][0]) and a[word[0]][0][:-2] in word:
                    a[word[0]].append(word)
        res = None
        for x in a.values():
            if not res:
                res = x[0]
            else:
                if len(x[0]) > len(res):
                    res = x[0]
                if len(x[0]) == len(res):
                    if ord(x[0][0]) < ord(res[0][0]):
                        res = x[0]
        return res

if __name__ == "__main__":
    # words = ["mo","m","moc","moch","mocha","l","la","lat","latt","latte","c","ca","cat"]
    # words = ["m","mo","moc","moch","mocha","l","la","lat","latt","latte","c","ca","cat"]
    words = ["a", "banana", "app", "appl", "ap", "apply", "apple",'apslyt']
    # words =["ogz","eyj","e","ey","hmn","v","hm","ogznkb","ogzn","hmnm","eyjuo","vuq","ogznk","og","eyjuoi","d"]
    print(Solution().longestWord(words))






