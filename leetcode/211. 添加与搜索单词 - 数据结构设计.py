class WordDictionary:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.words = []

    def addWord(self, word: str) -> None:
        """
        Adds a word into the data structure.
        """
        self.words.append(word)

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the data structure. A word could contain the dot character '.' to represent any one letter.
        """
        l = len(word)
        for tt in self.words:
            if len(tt) != len(word):
                continue
            flag = True
            for i in range(l):
                if word[i] == '.':
                    continue
                if word[i] != tt[i]:
                    flag = False
                    break
            if flag:
                return True
        return False

# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)
