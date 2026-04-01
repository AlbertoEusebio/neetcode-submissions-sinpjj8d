class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        for i in range(len(board)):
            digits = [1] * 10
            print(board[i])
            for c in board[i]:
                if c == '.':
                    continue
                c = int(c)
                digits[c] -= 1
                if digits[c] < 0:
                    return False

        for j in range(len(board[0])):
            digits = [1] * 10
            for i in range(len(board)):
                c = board[i][j]
                if c == '.':
                    continue
                c = int(c)
                digits[c] -= 1
                if digits[c] < 0:
                    return False

        i = 0
        while i < len(board):
            j = 0
            while j < len(board[0]):
                digits = [1] * 10
                for a in range(3):
                    for b in range(3):
                        c = board[i+a][j+b]
                        if c == '.':
                            continue
                        c = int(c)
                        digits[c] -= 1
                        if digits[c] < 0:
                            return False
                print(digits)
                j+=3
            i+=3
        
        return True