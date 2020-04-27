class Solution(object):
    def game(self, guess, answer):
        """
        :type guess: List[int]
        :type answer: List[int]
        :rtype: int
        """
        index = 0
        for i, j in zip(guess, answer):
            if i == j:
                index += 1
        return index

if __name__ == '__main__':
    guess = [2, 2, 3]
    answer = [3, 2, 1]
    s=Solution()
    print(s.game(guess,answer))

