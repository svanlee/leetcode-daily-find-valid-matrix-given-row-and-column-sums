from typing import List


class Solution:
    def restoreMatrix(self, rowSum: List[int], colSum: List[int]) -> List[List[int]]:
        # Create a copy of the input lists to avoid modifying the original lists
        col_sum = colSum.copy()
        row_sum = rowSum.copy()
        
        # Initialize the result matrix with all elements set to 0
        mat = [[0]*len(col_sum) for _ in range(len(row_sum))]
        
        # Initialize indices for the row and column
        i = j = 0
        
        # Loop until we've filled in the entire matrix
        while i < len(row_sum) and j < len(col_sum):
            # Assign the minimum of the current row sum and column sum to the current cell
            mat[i][j] = min(row_sum[i], col_sum[j])
            
            # Update the row sum and column sum
            row_sum[i] -= mat[i][j]
            col_sum[j] -= mat[i][j]
            
            # Move to the next cell
            if row_sum[i] == 0:
                i += 1
            if col_sum[j] == 0:
                j += 1
        
        # Return the completed matrix
        return mat