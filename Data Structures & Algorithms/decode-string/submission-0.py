class Solution:
    def decodeString(self, s: str) -> str:
        def dfs(s):

            # print(s)
            if len(s) == 1:
                return s
            res = ""
            num = ""

            i=0
            while i < len(s):
                c = s[i]
                if c in "1234567890":
                    num += c
                elif c == '[':
                    n = int(num)
                    cnt = 1
                    j = i+1
                    while j < len(s) and cnt:
                        if s[j] == '[':
                            cnt += 1
                        elif s[j] == ']':
                            cnt -= 1
                        j+=1
                    sub = s[i+1:j-1]
                    res += n*dfs(sub)
                    n=0
                    num = ""
                    print(res)
                    i = j-1
                else:
                    res += c
                i+=1
            return res
        return dfs(s)