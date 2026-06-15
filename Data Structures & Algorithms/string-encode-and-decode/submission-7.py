class Solution:

    def encode(self, strs: List[str]) -> str:
        lens = [len(s) for s in strs]

        st = ''
        for l, s in zip(lens, strs):
            st += f'{l}+{s}'

        return st

    def decode(self, s: str) -> List[str]:
        
        print(s)
        strs = []
        i = 0
        st = ''
        n = 0
        while i < len(s):
            if n == 0 and s[i].isnumeric():
                c = i
                while c < len(s) and s[c].isnumeric():
                    c+=1
                n = int(s[i:c])
                c+=1
                i = c
            st = s[i:i+n]
            strs.append(st)

            i += n
            n=0

        return strs