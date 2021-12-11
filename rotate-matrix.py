def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        n=len(matrix[0])
        sample=[ [0]*n for i in range(n)]
        for i in range(n):
            for j in range(n):
                sample[i][j]=matrix[n-1-j][i]
        return sample

matrix = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]
n=len(matrix[0])
sample=[[0]*n]*n

# sample[2][2]=matrix[2][1]



# for i in range(n):
#     sample[0][i]=i

# print(sample)
# out=rotate(7,matrix)
# print(out)

def transpose(matrix):
    for i in range(len(matrix)):
        for j in range(i,len(matrix[0])):
            matrix[i][j],matrix[j][i]=matrix[j][i],matrix[i][j]
    return matrix


def reverse(matrix):
    for i in range(len(matrix[0])//2):
        for j in range(len(matrix)):
            matrix[j][i],matrix[j][len(matrix[0])-i-1]=matrix[j][len(matrix[0])-i-1],matrix[j][i]
    return matrix

def rotate_matrix(matrix):
    transpose(matrix)
    reverse(matrix)
    return matrix

matrix = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]

print(rotate_matrix(matrix))

def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        for i in range()
        return matrix