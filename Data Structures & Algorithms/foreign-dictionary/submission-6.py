class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        
        prec = defaultdict(set)

        letters = set()

        for w in words:
            letters.update(set(w))

        for i in range(len(words)-1):
            w1,w2 = words[i], words[i+1]

            j = 0
            while j < min(len(w1), len(w2)) and w1[j] == w2[j]:
                j += 1

            if j == len(w2) and len(w1) > len(w2):
                return ""

            if j < min(len(w1), len(w2)):
                prec[w2[j]].add(w1[j])
            

        used = set()

        print(letters)
        print(prec)
        
        que = deque([])
        used = set()
        alph = ""

        for l in letters:
            if l not in prec:
                que.append(l)
                used.add(l)


        while que:
            c = que.popleft()
            alph += c

            for l in letters:
                if l not in used and l in prec and len(prec[l] - used) == 0:
                    que.append(l)
                    used.add(l)
        
        if len(used) < len(letters):
            return ""
        
        return alph