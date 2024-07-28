from typing import List


class Solution:
    def restoreMatrix(self, rowSum: List[int], colSum: List[int]) -> List[List[int]]:
        m, n = len(rowSum), len(colSum)
        res = [[0] * n for _ in range(m)]
        
        for i in range(m):
            for j in range(n):
                val = min(rowSum[i], colSum[j])
                res[i][j] = val
                rowSum[i] -= val
                colSum[j] -= val
            
        return res