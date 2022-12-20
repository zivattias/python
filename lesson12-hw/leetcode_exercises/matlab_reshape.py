# In MATLAB, there is a handy function called reshape which can reshape an m x n matrix into a new one
# with a different size r x c keeping its original data.
#
# You are given an m x n matrix mat and two integers r and c
# representing the number of rows and the number of columns of the wanted to be reshaped matrix.
#
# The reshaped matrix should be filled with all the elements of the original matrix
# in the same row-traversing order as they were.
#
# If the reshape operation with given parameters is possible and legal, output the new reshaped matrix;
# Otherwise, output the original matrix.


matrix = [[1, 2, 'a'], [3, 4, 'a'], [5, 6, 'a'], [7, 8, 'a'], [9, 10, 'a']]
#
r = 3
c = 5


def reshape(mat: list, row: int, col: int):
    if row * col != len(mat) * len(mat[0]):
        return mat

    else:
        result = []
        temp = []
        count = 0
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                # create a list with length of c
                temp.append(mat[i][j])
                count += 1
                if count == col:
                    # this makes sure it has the new c length
                    # append temp list to the result list
                    result.append(temp)
                    # reset temp list and counter
                    temp = []
                    count = 0
        return result


print(reshape(matrix, r, c))
