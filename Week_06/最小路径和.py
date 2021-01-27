class Solution:
    def minPathSum(self, grid: [[int]]) -> int:
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if i == j == 0: continue
                elif i == 0:  grid[i][j] = grid[i][j - 1] + grid[i][j]
                elif j == 0:  grid[i][j] = grid[i - 1][j] + grid[i][j]
                else: grid[i][j] = min(grid[i - 1][j], grid[i][j - 1]) + grid[i][j]
        return grid[-1][-1]

'''
时间复杂度 O(M \times N)O(M×N) ： 遍历整个 gridgrid 矩阵元素。
空间复杂度 O(1)O(1) ： 直接修改原矩阵，不使用额外空间。
'''