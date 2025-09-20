def count_islands(grid):
    """
    Count number of islands (connected 1s) in 2D grid using DFS.
    
    Time Complexity: O(M × N) where M = rows, N = columns
    - We visit each cell in the grid exactly once in the outer loops
    - DFS marks visited cells as '0', so each cell is processed at most once
    - Even though DFS can be recursive, total work across all DFS calls is O(M × N)
    
    Space Complexity: O(M × N) in worst case
    - Recursion stack depth can be M × N in worst case (entire grid is one island)
    - This happens when all cells are '1' and form a single connected component
    - In best case (no islands), space complexity is O(1)
    """
    if not grid or not grid[0]:
        return 0
    
    def dfs(i, j):
        # Base case: out of bounds or not land ('1')
        if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]) or grid[i][j] != '1':
            return
        
        # Mark current cell as visited by changing '1' to '0'
        grid[i][j] = '0'  # O(1) operation
        
        # Recursively explore all 4 directions (up, right, down, left)
        # Each direction leads to at most M×N recursive calls total across entire algorithm
        for di, dj in [(0,1), (1,0), (0,-1), (-1,0)]:
            dfs(i + di, j + dj)
    
    count = 0
    # Outer loops: O(M × N) - visit every cell once
    for i in range(len(grid)):           # M iterations
        for j in range(len(grid[0])):    # N iterations
            if grid[i][j] == '1':        # O(1) check
                dfs(i, j)                # Amortized O(1) per cell across all calls
                count += 1               # O(1) increment
    
    return count

# Test cases with complexity analysis
test_grids = [
    # Test Case 1: Single large island (worst case for space complexity)
    # Grid: 4×5, mostly connected - Space: O(M×N) due to deep recursion
    [["1","1","1","1","0"],
     ["1","1","0","1","0"],
     ["1","1","0","0","0"],
     ["0","0","0","0","0"]],  # Expected: 1 island
    
    # Test Case 2: Multiple small islands (better space complexity)
    # Grid: 4×5, scattered islands - Space: O(min island size)
    [["1","1","0","0","0"],
     ["1","1","0","0","0"],
     ["0","0","1","0","0"],
     ["0","0","0","1","1"]],  # Expected: 3 islands
    
    # Test Case 3: Individual islands (best case for space complexity)  
    # Grid: 3×5, no connections - Space: O(1) per DFS call
    [["1","0","1","0","1"],
     ["0","1","0","1","0"],
     ["1","0","1","0","1"]],  # Expected: 8 islands
]

# Complexity Summary:
# - Time: Always O(M × N) regardless of island distribution
# - Space: Varies from O(1) to O(M × N) depending on island connectivity

for i, grid in enumerate(test_grids):
    # Make copy since DFS modifies original grid (marking visited cells as '0')
    # Copy operation: O(M × N) time and space
    grid_copy = [row[:] for row in grid]
    result = count_islands(grid_copy)
    print(f"Grid {i+1}: {result} islands")
    # Expected output: Grid 1: 1 islands
    #                  Grid 2: 3 islands  
    #                  Grid 3: 8 islands

# Why Time Complexity is O(M × N):
# Each cell is visited exactly once by the outer loops: O(M × N)
# Each cell is processed by DFS at most once (marked as '0' when visited)
# Total work done by all DFS calls combined: O(M × N)
# Therefore: Overall time complexity = O(M × N)