class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        if len(matrix)==0:
            return []
        colStart = 0
        colEnd = len(matrix[0])-1
        rowStart = 0
        rowEnd = len(matrix)-1
        res = []
        while(colStart<=colEnd and rowStart<=rowEnd):
            # top line
            for i in range(colStart, colEnd+1):
                res.append(matrix[rowStart][i])
            rowStart+=1
            # right line
            for i in range(rowStart, rowEnd+1):
                res.append(matrix[i][colEnd])
            colEnd-=1
            # bottom line
            if rowStart<= rowEnd:
                for i in range(colEnd, colStart-1, -1):
                    res.append(matrix[rowEnd][i])
            rowEnd-=1
            # left line
            if colStart<=colEnd:
                for i in range(rowEnd, rowStart-1, -1):
                    res.append(matrix[i][colStart])
            colStart+=1

        return res
    
   # this problem can be rewritten to print from center to outside.
   # also this problem can be rewritten to set the matrix given the N
