class WordDictionary(object):
    def __init__(self):
        self.ret = []

    def addWord(self, word):
        self.ret.append(word)

    def search(self, word):
        import re
        for i in self.ret:
            x = re.search(word, i)
            if x and x.span()[0] == 0 and x.span()[1] == len(i):
                return True
        return False


# Your WordDictionary object will be instantiated and called as such:
obj = WordDictionary()
obj.addWord('at')
obj.addWord('and')
obj.addWord('an')
obj.addWord('add')
print(obj.search('a'))
print(obj.search('.at'))
print(obj.search('bat'))
