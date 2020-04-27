class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        num_b = text.count('b')
        num_o = text.count('o')
        num_a = text.count('a')
        num_l = text.count('l')
        num_n = text.count('n')
        n_l = num_l // 2
        n_o = num_o // 2
        ret = [num_a, num_b, num_n, n_l, n_o]
        a = min(ret)
        return a


if __name__ == "__main__":
    text = "leetcode"
    print(Solution().maxNumberOfBalloons(text))

















