class Solution(object):
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        if n ==0:
            return []
        matrix = []
        for i in range(n):
            matrix.append(list((0,)*n))
        res = [i for i in range(1, n*n+1)]
        count = 0
        rowBegin, rowEnd, colBegin, colEnd = 0, len(matrix) - 1, 0, len(matrix[0]) - 1
        while (rowBegin <= rowEnd and colBegin <= colEnd):
            for i in range(colBegin, colEnd + 1):
                matrix[rowBegin][i] = res[count]
                count += 1
            rowBegin += 1
            for i in range(rowBegin, rowEnd + 1):
                matrix[i][colEnd] = res[count]
                count += 1
            colEnd -= 1
            if rowBegin <= rowEnd:
                for i in range(colEnd, colBegin - 1, -1):
                    matrix[rowEnd][i] = res[count]
                    count += 1
            rowEnd -= 1
            if colBegin <= colEnd:
                for i in range(rowEnd, rowBegin - 1, -1):
                    matrix[i][colBegin] = res[count]
                    count += 1
            colBegin += 1
        return matrix
