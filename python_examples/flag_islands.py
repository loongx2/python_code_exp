def count_islands(grid):
    """Count number of islands (connected 1s) in 2D grid using DFS."""
    if not grid or not grid[0]:
        return 0
    
    def dfs(i, j):
        if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]) or grid[i][j] != '1':
            return
        grid[i][j] = '0'  # Mark as visited
        # Check all 4 directions
        for di, dj in [(0,1), (1,0), (0,-1), (-1,0)]:
            dfs(i + di, j + dj)
    
    count = 0
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == '1':
                dfs(i, j)
                count += 1
    return count

# Test cases
test_grids = [
    [["1","1","1","1","0"],
     ["1","1","0","1","0"],
     ["1","1","0","0","0"],
     ["0","0","0","0","0"]],  # Expected: 1
    
    [["1","1","0","0","0"],
     ["1","1","0","0","0"],
     ["0","0","1","0","0"],
     ["0","0","0","1","1"]],  # Expected: 3
    
    [["1","0","1","0","1"],
     ["0","1","0","1","0"],
     ["1","0","1","0","1"]],  # Expected: 9
]

for i, grid in enumerate(test_grids):
    # Make copy since DFS modifies original
    grid_copy = [row[:] for row in grid]
    result = count_islands(grid_copy)
    print(f"Grid {i+1}: {result} islands")
    # Expected output: Grid 1: 1 islands
    #                  Grid 2: 3 islands  
    #                  Grid 3: 8 islands