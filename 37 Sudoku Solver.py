class Solution(object):
    def solveSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        def isValid(board, row, col, num):
            for i in range(9):
                if board[i][col] != '.' and board[i][col] == num:
                    return False
                if board[row][i] != '.' and board[row][i] == num:
                    return False
                if board[3*(row/3)+i/3][3*(col/3) + i%3] != '.' and board[3*(row/3) + i/3][3*(col/3) + i%3] == num:
                    return False
            return True

        def solve(board):
            for i in range(9):
                for j in range(9):
                    if board[i][j] =='.':
                        for c in range(1,10):
                            num = str(c)
                            if isValid(board, i, j, num):
                                board[i][j] = num
                                if solve(board):
                                    return True
                                else:
                                    board[i][j] = '.'
                        return False
            return True
        
        solve(board)
