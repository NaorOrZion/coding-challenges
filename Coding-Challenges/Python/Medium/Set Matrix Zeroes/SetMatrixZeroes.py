class Solution(object):
    def setZeroes(self, matrix):
        listRowZero = []
        listColumnZero = []
        #Search for all zero indexes
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if matrix[i][j] == 0:
                    listRowZero.append(i)
                    listColumnZero.append(j)
        
        for i in listRowZero:
            for j in range(len(matrix[i])):
                matrix[i][j] = 0
                
        for i in listColumnZero:
            for j in range(len(matrix)):
                matrix[j][i] = 0
                