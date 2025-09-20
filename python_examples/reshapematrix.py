"""
MATRIX FLATTENING AND RESHAPING - COMPLETE TUTORIAL

This program demonstrates two approaches to flatten and reshape matrices:
1. Pure Python approach using list comprehensions and slicing
2. NumPy approach using built-in array methods

LEARNING OBJECTIVES:
- Understand matrix flattening (2D → 1D conversion)
- Learn matrix reshaping (changing dimensions while preserving data)
- Compare Pure Python vs NumPy performance and syntax
- Verify equivalence between different approaches

PREREQUISITES:
- Basic Python knowledge (lists, loops, slicing)
- NumPy library installed: pip install numpy
- Understanding of 2D arrays/matrices concept

PERFORMANCE NOTES:
- Pure Python: O(n) time, requires explicit iteration
- NumPy: Often O(1) for views, O(n) for copies, highly optimized C code
- NumPy is preferred for large matrices due to memory efficiency
"""

import numpy as np

def test_matrix_operations():
    """
    Test function to demonstrate matrix flattening and reshaping
    
    STEP-BY-STEP PROCESS:
    Step 1: Create a 2D matrix using nested lists
    Step 2: Display the original matrix structure
    Step 3: Flatten matrix using Pure Python (list comprehension)
    Step 4: Reshape flattened data back to 2D using Pure Python
    Step 5: Convert to NumPy and demonstrate NumPy operations
    Step 6: Show various NumPy reshaping options (1D, 2D, column vector)
    Step 7: Verify that both methods produce equivalent results
    
    TIME COMPLEXITY NOTES:
    - Pure Python flattening: O(rows × cols) - must iterate through all elements
    - NumPy reshaping: O(1) - creates views, no data copying
    - NumPy flattening: O(n) - may create copy depending on memory layout
    """
    
    print("=== Matrix Flattening and Reshaping Demo ===\n")
    # Expected output: === Matrix Flattening and Reshaping Demo ===
    
    # STEP 1: Create a sample 2D matrix using nested lists
    # This represents a 3x3 matrix with values 1-9
    original_matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    
    # STEP 2: Display the original matrix structure
    print("Original 2D matrix:")
    # Expected output: Original 2D matrix:
    for row in original_matrix:
        print(row)
    # Expected output: [1, 2, 3]
    #                  [4, 5, 6]
    #                  [7, 8, 9]
    
    # STEP 3: Pure Python flattening using list comprehension
    print("\n--- Pure Python ---")
    # Expected output: 
    #                  --- Pure Python ---
    
    # Flatten using nested list comprehension: outer loop for rows, inner loop for items
    flat_list = [item for row in original_matrix for item in row]
    print(f"Flattened: {flat_list}")
    # Expected output: Flattened: [1, 2, 3, 4, 5, 6, 7, 8, 9]
    
    # STEP 4A: Pure Python reshaping (keep as 1D - no change needed)
    reshaped_1d = flat_list  # 1D is already flat, just assign reference
    print(f"Reshaped to 1D: {reshaped_1d}")
    # Expected output: Reshaped to 1D: [1, 2, 3, 4, 5, 6, 7, 8, 9]
    
    # STEP 4B: Pure Python reshaping back to 3x3 matrix
    # Use slicing to take chunks of 3 elements to form each row
    reshaped_3x3 = []
    for i in range(0, len(flat_list), 3):  # Step by 3 to get row boundaries
        reshaped_3x3.append(flat_list[i:i+3])  # Take slice of 3 elements
    print("Reshaped back to 3x3:")
    # Expected output: Reshaped back to 3x3:
    for row in reshaped_3x3:
        print(row)
    # Expected output: [1, 2, 3]
    #                  [4, 5, 6]
    #                  [7, 8, 9]
    
    # STEP 5: NumPy operations - more efficient for large matrices
    print("\n--- NumPy ---")
    # Expected output: 
    #                  --- NumPy ---
    
    # Convert original matrix to NumPy array for efficient operations
    np_matrix = np.array(original_matrix)
    print(f"Original NumPy matrix:\n{np_matrix}")
    # Expected output: Original NumPy matrix:
    #                  [[1 2 3]
    #                   [4 5 6]
    #                   [7 8 9]]
    
    # NumPy flattening - creates a copy of the data in 1D
    flat_np = np_matrix.flatten()
    print(f"Flattened: {flat_np}")
    # Expected output: Flattened: [1 2 3 4 5 6 7 8 9]
    
    # STEP 6A: NumPy reshaping to different dimensions
    # Reshape 3x3 matrix to 1x9 (single row with 9 columns)
    reshaped_1x9 = np_matrix.reshape(1, 9)
    print(f"Reshaped to 1x9:\n{reshaped_1x9}")
    # Expected output: Reshaped to 1x9:
    #                  [[1 2 3 4 5 6 7 8 9]]
    
    # STEP 6B: Reshape to column vector (9 rows, 1 column)
    reshaped_9x1 = np_matrix.reshape(9, 1)
    print(f"Reshaped to 9x1:\n{reshaped_9x1}")
    # Expected output: Reshaped to 9x1:
    #                  [[1]
    #                   [2]
    #                   [3]
    #                   [4]
    #                   [5]
    #                   [6]
    #                   [7]
    #                   [8]
    #                   [9]]
    
    # STEP 6C: Reshape flattened array back to original 3x3 dimensions
    reshaped_back = flat_np.reshape(3, 3)
    print(f"Reshaped back to 3x3:\n{reshaped_back}")
    # Expected output: Reshaped back to 3x3:
    #                  [[1 2 3]
    #                   [4 5 6]
    #                   [7 8 9]]
    
    # STEP 7: Verify that both methods produce equivalent results
    print("\n--- Verification ---")
    # Expected output: 
    #                  --- Verification ---
    
    # Compare Pure Python and NumPy flattening results
    print(f"Pure Python and NumPy flattening equivalent: {flat_list == flat_np.tolist()}")
    # Expected output: Pure Python and NumPy flattening equivalent: True
    
    # Verify original matrix equals the reshaped result
    print(f"Original and reshaped matrices equivalent: {np.array_equal(np_matrix, reshaped_back)}")
    # Expected output: Original and reshaped matrices equivalent: True
    
    """
    SUMMARY OF STEPS COMPLETED:
    ✓ Step 1: Created 3x3 matrix using nested lists
    ✓ Step 2: Displayed original matrix structure  
    ✓ Step 3: Flattened matrix using Pure Python list comprehension
    ✓ Step 4A: Kept 1D format (no reshaping needed)
    ✓ Step 4B: Reshaped back to 3x3 using Pure Python slicing
    ✓ Step 5: Converted to NumPy array and flattened
    ✓ Step 6A: Reshaped to 1x9 matrix (single row)
    ✓ Step 6B: Reshaped to 9x1 matrix (column vector)
    ✓ Step 6C: Reshaped back to original 3x3 dimensions
    ✓ Step 7: Verified equivalence between Pure Python and NumPy results
    
    KEY TAKEAWAYS:
    - Pure Python: More verbose but educational, good for small matrices
    - NumPy: Concise, efficient, handles memory better for large data
    - Both approaches yield identical results when implemented correctly
    - NumPy reshaping is often just creating views (no data copying)
    """

if __name__ == "__main__":
    test_matrix_operations()