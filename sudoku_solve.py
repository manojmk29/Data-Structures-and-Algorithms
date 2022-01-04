class Solution(object):
    def solveSudoku(self, matrix):
        """
        :type board: List[List[str]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
        def safe(matrix,i,j,val):
            for k in range(9):
                if(matrix[k][j]==val):
                    return(False)
                if(matrix[i][k]==val):
                    return(False)
                if(matrix[((i//3)*3)+(k//3)][(3*(j//3))+(k%3)]==val):
                    return(False)
            return(True)
        def helper(board):
            for i in range(9):
                for j in range(9):
                    if(board[i][j]=="."):
                        for k in range(1,10):
                            if(safe(board,i,j,str(k))==True):
                                board[i][j]=str(k)
                                if(helper(board)==True):
                                    return(True)
                                else:
                                    board[i][j]="."
                        return(False)
            return(True)
        return(helper(matrix))
s=Solution()
matrix=[[".","8","7","6","5","4","3","2","1"],["2",".",".",".",".",".",".",".","."],["3",".",".",".",".",".",".",".","."],["4",".",".",".",".",".",".",".","."],["5",".",".",".",".",".",".",".","."],["6",".",".",".",".",".",".",".","."],["7",".",".",".",".",".",".",".","."],["8",".",".",".",".",".",".",".","."],["9",".",".",".",".",".",".",".","."]]
print(s.solveSudoku(matrix))