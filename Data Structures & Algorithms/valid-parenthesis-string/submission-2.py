class Solution:
    def checkValidString(self, s: str) -> bool:
        
        par = []
        stars = []

        for i,c in enumerate(s):
            if c == '(':
                par.append(i)
            elif c == '*':
                stars.append(i)
            elif c == ')':
                if len(par) > 0 and i > par[-1]:
                    par.pop()
                elif len(stars) >0 and i > stars[-1]:
                    stars.pop()
                else:
                    return False
        
        while par and stars:
            i = par.pop()
            j = stars.pop()

            if i > j:
                return False

        return len(par) == 0
