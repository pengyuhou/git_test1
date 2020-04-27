digits='23'

class Solution(object):
    def letterCombinations(self, digits):
        KEY={
            "2":list('abc'),
            '3':list('def'),
            '4':list('ghi'),
            '5':list('jkl'),
            '6':list('mno'),
            '7':list('pqrs'),
            '8':list('tuv'),
            '9':list('wxyz')
        }
        if list(digits) == None:
            return []


if __name__ =="__main__":
    solution=Solution()
    (solution.letterCombinations(digits))

