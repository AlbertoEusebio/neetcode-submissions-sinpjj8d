class Solution:
    def partition(self, s: str) -> List[List[str]]:
        
        def is_pal(s):
            i, j = 0, len(s) - 1

            while i < j:
                if s[i] != s[j]:
                    return False

                i += 1
                j -= 1
            return True

        res = []
        def dfs(i, j, s, path):
            
            if j > i or i > len(s):
                print(path)
                res.append(path.copy())
                return

            print(j, i, s, path, s[j:i])

            while i <= len(s):
                if is_pal(s[j:i]):
                    path.append(s[j:i])
                    dfs(i+1, i, s, path.copy())
                    path.pop()
                i+=1                
            
        dfs(1,0, s, [])

        return res