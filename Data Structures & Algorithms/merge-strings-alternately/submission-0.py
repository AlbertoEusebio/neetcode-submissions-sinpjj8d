class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        
        f=1
        i,j = 0,0
        s=""

        l1, l2 = len(word1), len(word2)

        while i<l1 and j< l2:

            if f:
                s+= word1[i]
                i+=1
            else:
                s+= word2[j]
                j+=1
            f=1-f
        
        while i<l1:
            s+= word1[i]
            i+=1
        
        while j<l2:
            s+=word2[j]
            j+=1
        
        return s