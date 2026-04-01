class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        
        stack = []

        for c in tokens:

            print(stack)
            if c in '+-/*':
                print(c)
                # Handle stack operation
                r = stack.pop()
                l = stack.pop()

                if c == '+':
                    res = l + r
                elif c == '-':
                    res = l - r
                elif c == '/':
                    res = abs(l) // abs(r)
                    res *= -1 if l*r < 0 else 1
                elif c == '*':
                    res = l * r
                stack.append(res)
            else:
                stack.append(int(c))

        return stack.pop()