class Solution:
    def topKFrequent(self, words, k: int):
        a = {}
        # 这一步排序是为了按照字母的大小排序
        words.sort()
        for word in words:
            if word not in a.keys():
                a[word] = 1
            else:
                a[word] += 1

        res = sorted(a.items(), key=lambda x: x[1],reverse=True)
        print(res)
        return  [i for i,j in res[:k]]


if __name__ == "__main__":
    words = ["i", "love", "leetcode", "i", "love", "coding"]

    # print(words)

    k = 3
    print(Solution().topKFrequent(words, k))
