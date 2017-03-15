class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        rowNums = {}
        colNums = {}
        cubNums = {}
        for i in range(9):
            for j in range(9):
              if board[i][j]!='.':
                  num = int(board[i][j])
                  cube = i/3*3+j/3
                  if (i, num) in rowNums.keys() or (j, num) in colNums.keys() or (cube, num) in cubNums.keys():
                      return False
                  rowNums[(i, num)] = True
                  colNums[(j, num)] = True
                  cubNums[(cube, num)] = True
        return True
