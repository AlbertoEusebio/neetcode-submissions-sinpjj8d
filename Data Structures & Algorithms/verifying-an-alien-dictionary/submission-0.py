class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        dc = {}
        
        for i,c in enumerate(order):
            dc[c] = i
        
        # compare 1 with 0 and so on
        j = 1
        while j < len(words):
            w1 = words[j-1]
            w2 = words[j]

            m_l = min(len(w1), len(w2))

            a = 0
            b = 0

            for k in range(m_l):
                a += dc[w1[k]]
                b += dc[w2[k]]

                if a > b:
                    return False
                elif a < b:
                    break # these are sorted
                # continue if equal characters
            
            if a == b:
                # w1 longer but equal tio w2
                if len(w1) > len(w2):
                    return False

            j += 1
        return True