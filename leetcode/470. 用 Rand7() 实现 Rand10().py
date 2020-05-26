# The rand7() API is already defined for you.
def rand7():
    pass


# @return a random integer in the range 1 to 7

class Solution:
    def rand10(self):
        import random
        return random.randint(1, 10)


import random

print(random.randint(1, 10))
