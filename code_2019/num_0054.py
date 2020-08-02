class Solution:
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        m = len(matrix)
        n = len(matrix[0])
        calculate = 2*m +2*n -4
        all = m*n
        count = 0
        current_row = 0
        current_col = 0
