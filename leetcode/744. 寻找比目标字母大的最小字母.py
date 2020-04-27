class Solution(object):
    def nextGreatestLetter(self, letters, target):
        ret=[]
        for letter in letters:
            if letter > target:
                ret.append(letter)
        if ret:
            return min(ret)
        else:
            return min(letters)


if __name__== "__main__":
    a= ["c", "f", "j"]
    b= "j"
    
    print(Solution().nextGreatestLetter(a,b))








