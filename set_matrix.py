def setZeroes(matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        row_len=len(matrix)
        col_len=len(matrix[0])
        for i in range(row_len):
            for j in range(col_len):
                if(matrix[i][j]==0):
                    matrix[i][0]=matrix[0][j]=0
        for i in range(row_len):
            for j in range(col_len):
                if(matrix[i][0]==0 or matrix[0][j]==0):
                    matrix[i][j]=0