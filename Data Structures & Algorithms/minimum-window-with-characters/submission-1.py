class Solution:
    def minWindow(self, s: str, t: str) -> str:
        occur = defaultdict(int)
        sm = 0

        if s == t:
            return t

        def is_ok(di):
            tot = 0
            for k, v in di.items():
                if v > 0:
                    return False
            return True

        for c in t:
            occur[c] += 1
            sm += 1
        
        res = ""

        print(occur)

        i=0
        j=0
        while i < len(s):
            c = s[i]
            if c in occur:
                occur[c] -= 1
            
            while is_ok(occur) and j <= i:
                res = s[j:i+1] if ((i-j) < len(res) or res == '') else res
                if s[j] in occur:
                    occur[s[j]] += 1
                j+=1

            # print(occur, res, j, i)

            i += 1 

        if is_ok(occur):
            print(occur, j, i)
            
            while is_ok(occur) and j < i:
                if s[j] in occur:
                    occur[s[j]] += 1
                j+=1

            st = s[j:i+1]
            
            if res == "" or len(res) < len(st):
                res = st
            
        return res