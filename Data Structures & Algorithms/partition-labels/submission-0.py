class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        lett = defaultdict(int)

        for c in s:
            lett[c] += 1

        subs = []
        sub = ""
        for c in s:
            sub += c
            lett[c] -= 1

            all_done = True
            for l in sub:
                if lett[l] != 0:
                    all_done = False
                    break
            if all_done:
                subs.append(len(sub))
                sub = ''
        
        return subs