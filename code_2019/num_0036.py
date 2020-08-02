class Solution:
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        for b in board:
            dotnum = b.count(".")
            if dotnum+len(set(b)) < 10:
                return False
        for z in zip(*board):
            dotnum = z.count(".")
            if dotnum+len(set(z)) < 10:
                return False
        for i in range(3):
            for j in range(3):
                vals = []
                vals.extend(board[i*3][j*3:j*3+3])
                vals.extend(board[i*3+1][j*3:j*3+3])
                vals.extend(board[i*3+2][j*3:j*3+3])
                dotnum = vals.count(".")
                if dotnum+len(set(vals)) < 10:
                    return False
        return True
