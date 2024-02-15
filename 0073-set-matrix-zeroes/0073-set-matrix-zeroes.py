class Solution:
    def setZeroes(self, matrix) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        columnZero = False
        rowZero = False
        if matrix[0][0]==0:
            rowZero=True
            columnZero=True
        for i in range(len(matrix)):
            if matrix[i][0]==0:
                matrix[i][0]=True
                columnZero=True
        for i in range(len(matrix[0])):
            if matrix[0][i] == 0 or matrix[0][i] is True:
                matrix[0][i]=True
                rowZero = True

        for i in range(1,len(matrix)):
            for j in range(1,len(matrix[0])):
                if matrix[i][j]==0:
                    matrix[0][j]=True
                    matrix[i][0]=True
        for i in range(1, len(matrix)):
            for j in range(1, len(matrix[0])):
                if matrix[i][0] is True or matrix[0][j] is True:
                    matrix[i][j]=0
        
        if columnZero is True:
            for i in range(len(matrix)):
                matrix[i][0] = 0
        else:
            for i in range(len(matrix)):
                if matrix[i][0] is True:
                    matrix[i][0]=0
        if rowZero is True:
            for i in range(len(matrix[0])):
                matrix[0][i] = 0
        else:
            for i in range(len(matrix[0])):
                if matrix[0][i] is True:
                    matrix[0][i]=0