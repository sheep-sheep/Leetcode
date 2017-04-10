class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        if not board:
            return False
        for row in range(len(board)):
            for col in range(len(board[0])):
                if self.dfs(board, row, col, word):
                    return True
        return False

    def dfs(self, board, row, col, word):
        # find word starting at (row, col)
        if len(word) == 0: # nothing to check within the word
            return True
        if row<0 or row >=len(board) or col < 0 or col >= len(board[0]) or word[0]!=board[row][col]:
            return False

        tmp = board[row][col]
        board[row][col] = "#"  # avoid visit agian 
        res = self.dfs(board, row+1, col, word[1:]) or self.dfs(board, row-1, col, word[1:])\
                or self.dfs(board, row, col+1, word[1:]) or self.dfs(board, row, col-1, word[1:])

        board[row][col] = tmp # assign the value back to remove the mark
        return res
