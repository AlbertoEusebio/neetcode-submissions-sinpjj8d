class Solution:

    def encode(self, strs: List[str]) -> str:
        # Encode len#string
        s = ''

        for st in strs:
            s += f'{len(st)}#{st}'

        return s

    def decode(self, s: str) -> List[str]:
        strs = []

        i = 0
        j = 0

        st = ''
        l = 0
        INIT = False

        # 5#abbad

        while j < len(s):
            c = s[j]
            
            if c == '#' and not INIT:
                l = int(s[i:j])
                INIT = True
            else:
                if l > 0:
                    st += c
                    l -= 1
                elif INIT:
                    i = j
                    strs.append(st)
                    st = ''
                    INIT = False

            j+=1

        if INIT:
            strs.append(st)

        return strs