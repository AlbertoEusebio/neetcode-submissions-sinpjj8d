class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        
        n = len(coins)
        res = []

        memo = {}

        def dfs(i, path, tot):
            
            if i >= n and tot != amount:
                return 0
            elif tot == amount:
                print("Take: ", i)
                # if path in res:
                #     return 0
                res.append(path)
                
                return 1

            if (i, tot) in memo:
                return memo[(i, tot)]

            print(coins[i])
            # takes
            a, b = 0,0
            if tot + coins[i] <= amount:
                path.append(coins[i])
                b = dfs(i, path.copy(), tot + coins[i]) # take no move
                a = dfs(i+1, path.copy(), tot + coins[i]) # take
                path.pop()
            # take or not

            c = dfs(i+1, path.copy(), tot) # no take

            memo[(i, tot)] = sum([max(a,b),c])

            return sum([max(a,b),c])

        a = dfs(0, [], 0)

        print(res)
        return a
