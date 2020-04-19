class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if not r and not c: continue
                if r-1<0: grid[r][c] += grid[r][c-1]
                elif c-1<0: grid[r][c] += grid[r-1][c]
                else: grid[r][c] += min(grid[r-1][c],grid[r][c-1])
        return grid[len(grid)-1][len(grid[0])-1]
