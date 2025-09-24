def fire(grid,i,j):
    if i<0 or j<0 or i>=len(grid) or j>=len(grid[0]) or grid[i][j]!=0:
        return
    grid[i][j]=2
    fire(grid,i+1,j) #down
    fire(grid,i-1,j) #up
    fire(grid,i,j+1) #right
    fire(grid,i,j-1) #left
    return grid

matrix=[[0,1,0,0,0],
        [0,1,0,1,0],
        [0,1,0,1,0],
        [1,0,0,1,1],]
result=fire(matrix,0,0)
print(result)