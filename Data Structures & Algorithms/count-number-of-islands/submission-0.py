class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        visited = set()
        directions = [(1, 0), (-1, 0), (0, -1), (0, 1)]
        rows = len(grid)
        cols = len(grid[0])
        islands = 0

        def dfs(r, c):
            if (r, c) in visited:
                return
            
            if r < 0 or r >= rows or c < 0 or c >= cols:
                return
            
            if grid[r][c] == '0':
                return
            
            visited.add((r, c))
            
            for dr, dc in directions:
                dfs(r + dr, c + dc)
            

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == '1' and (i, j) not in visited:
                    islands += 1
                    dfs(i, j)
        
        return islands