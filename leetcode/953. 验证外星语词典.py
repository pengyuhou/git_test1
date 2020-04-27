class Solution(object):
    def isAlienSorted(self, words, order):
        return words==sorted(words, key=lambda w: [order.index(x) for x in w])

if __name__ == "__main__":
    words = ['word', 'world','who','wordless','row']
    order = "hlabcdefgijkmnopqrstuvwxyz"
    print(Solution().isAlienSorted(words,order))




    # a = {}
    # for word in words:
    #     if word[0] not in a.keys():
    #         a[word[0]] = [word]
    #     else:
    #         a[word[0]].append(word)
    # print(a)






















    # sorted(words,key=lambda x:order.index())

