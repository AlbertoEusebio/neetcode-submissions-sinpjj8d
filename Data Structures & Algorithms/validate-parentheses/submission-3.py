class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        parenthesis_o = "([{"
        parenthesis_c = ")]}"


        for c in s:
            if c in parenthesis_o:
                stack.append(c)
            elif c in parenthesis_c:
                if len(stack) > 0 and stack[-1] == parenthesis_o[parenthesis_c.index(c)]:
                    print(c, parenthesis_o[parenthesis_c.index(c)])
                    stack = stack[:-1]
                else:
                    return False
            
        if len(stack) == 0:
            return True
        
        return False