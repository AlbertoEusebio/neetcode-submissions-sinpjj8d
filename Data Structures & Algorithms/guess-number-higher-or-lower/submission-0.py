# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        i,j= 0, n
        m = (i+j)//2
        while i<j:
            if guess(m) > 0:
                i = m+1
            elif guess(m) < 0:
                j = m-1
            elif guess(m) == 0:
                return m

            m = (i+j)//2

        return m