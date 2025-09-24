class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        def fire(i,j):
            if i<0 or j<0 or i>=len(grid) or j>=len(grid[0]) or grid[i][j]!='1':
                return
            grid[i][j]=2
            fire(i+1,j) #down
            fire(i-1,j) #up
            fire(i,j+1) #right
            fire(i,j-1) #left  
        num_islands=0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]=='1':
                    num_islands+=1
                    fire(i,j)
        return num_islands
