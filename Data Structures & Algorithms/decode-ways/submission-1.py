class Solution:
    def numDecodings(self, s: str) -> int:
        

        letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        data ={}
        for i, l in enumerate(letters):
            data[str(i+1)] = l

        # print(data)

        def dfs(i, j):

            if i >= len(s):
                return 0
            elif j == len(s):
                if s[i:j] not in data:
                    return 0
                # print(i, j, 'Taan lett:', s[i:j])
                
                return 1

            # print(i, j, 'lett:', s[i:j])
            # decode s[i:j]
            if s[i:j] not in data:
                return 0

            m = dfs(j, j+1) + dfs(j, j+2)
            
            return m

        return dfs(0, 1) + dfs(0, 2)