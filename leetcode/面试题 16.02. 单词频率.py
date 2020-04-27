class WordsFrequency:

    def __init__(self,li):
        self.a = {}
        for t in li:
            if t not  in self.a.keys():
                self.a[t]=1
            else:
                self.a[t] += 1


    def get(self, word: str) -> int:
        if word  not in self.a.keys():
            return 0
        else:
            return self.a[word]



# Your WordsFrequency object will be instantiated and called as such:
# obj = WordsFrequency(book)
# param_1 = obj.get(word)

if __name__ == "__main__":
    a=WordsFrequency(["i", "have", "an", "apple", "he", "have", "a", "pen"])
    print(a.get('have'))



