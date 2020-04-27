class Solution(object):
    def f(self,word):
        return word.count(min(word))
    def numSmallerByFrequency(self, queries, words):
        ret=[]
        for word in words:
            ret.append(self.f(word))
        res=[]
        for query in queries:
            a=0
            i=1
            while self.f(query)+i<=max(ret):
                a += ret.count(self.f(query)+i)
                i += 1
            res.append(a)
        return res


if __name__ == "__main__":
    queries = ["bbb", "cc"]
    words = ["a", "aa", "aaa", "aaaa"]
    queries = ["cbd"]
    words = ["zaaaz"]
    # queries = ["cbd"]
    # words = ["zaaaz"]
    print(Solution().numSmallerByFrequency(queries,words))






