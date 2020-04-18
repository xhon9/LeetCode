class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if len(grid)<1: return 0

        def dfs(r, c):
            if r<0 or c<0 or r>len(grid)-1 or c>len(grid[0])-1 or grid[r][c]=='0': return
            grid[r][c] = '0'
            dfs(r-1, c); dfs(r+1, c); dfs(r, c-1); dfs(r, c+1)

        cont = 0
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c]=='0': continue
                else: cont+=1; dfs(r,c)
        return cont
