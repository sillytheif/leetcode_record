class Solution:
    def numIslands(self, grid):
        if not grid: return 0
        m, n, count = len(grid[0]), len(grid), 0
        for i in range(n):
            for j in range(m):
                if grid[i][j] == '1':
                    count += 1
                    self.mark(grid, i, j)
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 'X': grid[i][j] = '1'
        return count

    def mark(self, grid, row, col):
        grid[row][col] = 'X'
        m, n = len(grid[0]), len(grid)
        for dirc in [[0, 1], [0, -1], [1, 0], [-1, 0]]:
            if 0 <= (row + dirc[0]) < n and 0 <= (col + dirc[1]) < m \
                    and grid[row + dirc[0]][col + dirc[1]] == '1':
                self.mark(grid, row + dirc[0], col + dirc[1])

class Solution:
    def numIslands(self, grid):
        def dfs(grid,i,j):
            grid[i][j]='0'
            if i>0 and grid[i-1][j]=='1':
                dfs(grid,i-1,j)
            if j>0 and grid[i][j-1]=='1':
                dfs(grid,i,j-1)
            if i<m-1 and grid[i+1][j]=='1':
                dfs(grid,i+1,j)
            if j<n-1 and grid[i][j+1]=='1':
                dfs(grid,i,j+1)
        m,n = len(grid),len(grid[0])
        count =0
        for i in range(m):
            for j in range(n):
                if grid[i][j]=='1':
                    count+=1
                    dfs(grid,i,j)
        return count

