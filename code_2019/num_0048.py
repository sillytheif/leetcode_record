class Solution:
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        for i in range(n):
            for j in range(i+1,n):
                matrix[i][j],matrix[j][i] = matrix[j][i],matrix[i][j]
        print(matrix)
        for i in range(n):
            head, end = 0,n-1
            while head<end:
                matrix[i][head],matrix[i][end] = matrix[i][end],matrix[i][head]
                head +=1
                end  -=1
        return matrix

a= Solution()
print(a.rotate([
  [1,2,3],
  [4,5,6],
  [7,8,9]
]))

