# class Solution(object):
#     def exist(self, board, word):
#         """
#         :type board: List[List[str]]
#         :type word: str
#         :rtype: bool
#         """
#         def exist(board, used, i, j, part):
#             if len(part)==0: return True
#             if j+1<len(board[0]) or j-1>=0 or i+1<len(board) or i-1>=0 : return False
#             if board[i][j] != part[0] or used[i][j]: return False
#             used[i][j] = True
#             return exist(board, used, i, j+1, part[1:])or \
#                    exist(board, used, i, j-1, part[1:])or \
#                    exist(board, used, i+1, j, part[1:])or \
#                    exist(board, used, i-1, j, part[1:])


#         rowN = len(board)
#         colN = len(board[0])
#         used = [[False]*colN for _ in range(rowN)]
#         for i in range(rowN):
#             for j in range(colN):
#                 if exist(board, used, i, j, word): return True
#         return False
    
# Use one board but need to change it and assign the value back
# Use ^256 to operate on char 
