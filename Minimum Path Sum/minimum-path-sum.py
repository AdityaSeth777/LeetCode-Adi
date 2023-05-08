class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        n=len(grid)
        m=len(grid[0])
        for i in range(n):
            for j in range(m):
                if i==0:
                    if j!=0:
                        grid[i][j]+=grid[i][j-1]
                elif j==0:
                    if i!=0:
                        grid[i][j]+=grid[i-1][j]
                else:
                    grid[i][j]+=min(grid[i-1][j],grid[i][j-1])
        return grid[n-1][m-1]