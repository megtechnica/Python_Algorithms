## Given a m x n grid filled with integers, find the submatrix with maximum sum among all submatrices.

class Solution:

    def get(self, grid, i, j):
        if i >= 0 and i < len(grid) and j >= 0 and j < len(grid[0]):
            return grid[i][j]
        return 0
        
    def maxSum(self, grid):
        result = grid[0][0]
        partialSums = [[0 for _ in range(len(grid[0]))] for _ in range(len(grid))]
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                partialSums[i][j] = grid[i][j] + \
                                    self.get(partialSums, i - 1, j) + \
                                    self.get(partialSums, i, j - 1) - \
                                    self.get(partialSums, i - 1, j - 1)

        for x1 in range(len(grid)):
            for y1 in range(len(grid[0])):
                for x2 in range (x1, len(grid)):
                    for y2 in range(y1, len(grid[0])):
                        sum =   self.get(partialSums, x2, y2) - \
                                self.get(partialSums, x1 - 1, y2) - \
                                self.get(partialSums, x2, y1 - 1) + \
                                self.get(partialSums, x1 - 1, y1 - 1)
                        result = max(result, sum)
        return result
