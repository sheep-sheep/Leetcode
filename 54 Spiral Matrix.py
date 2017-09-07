class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        res = []
        if not matrix:
            return res
        rowBegin, rowEnd, colBegin, colEnd = 0, len(matrix)-1, 0, len(matrix[0])-1
        while(rowBegin<=rowEnd and colBegin<=colEnd):
            for i in range(colBegin, colEnd+1):
                res += [matrix[rowBegin][i]]
            rowBegin+=1
            for i in range(rowBegin, rowEnd+1):
                res += [matrix[i][colEnd]]
            colEnd-=1
            if rowBegin<= rowEnd:
                for i in range(colEnd, colBegin-1, -1):
                    res += [matrix[rowEnd][i]]
            rowEnd-=1
            if colBegin<=colEnd:
                for i in range(rowEnd, rowBegin-1, -1):
                    res += [matrix[i][colBegin]]
            colBegin+=1
        return res
rowEnd = row_n-1
res = []
while(colStart < colEnd):
    res.append(matrix[rowStart][colStart])
    colStart += 1
rowStart += 1
while(rowStart < rowEnd):
    res.append(matrix[rowStart][colStart])
    rowStart += 1
colStart -= 1
while(colStart >= 0):
    res.append(matrix[rowStart][colStart])
    colStart -= 1
rowStart -= 1
while(rowStart >= 0):
    res.append(matrix[rowStart][colStart])
    rowStart -= 1
colStart += 1
