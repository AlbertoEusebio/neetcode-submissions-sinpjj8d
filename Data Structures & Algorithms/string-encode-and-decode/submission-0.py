class Solution:

    def encode(self, strs: List[str]) -> str:
        s = ''
        for st in strs:
            s += st + '\0' 
        return s

    def decode(self, s: str) -> List[str]:
        strs = []

        st = ''
        for c in s:
            if c == '\0':
                strs.append(st)
                st = ''
            else:
                st += c
        return strs
            