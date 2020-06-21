#
# @lc app=leetcode.cn id=221 lang=python3
#
# [221] 最大正方形
#


# @lc code=start
class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        if not matrix:
            return 0
        col = len(matrix)
        row = len(matrix[0])
        max_side = 0
        DP = [[0 for _ in range(row + 1)] for _ in range(col + 1)]
        print(DP)
        for i in range(col):
            for j in range(row):
                if matrix[i][j] == '1':
                    DP[i + 1][j + 1] = min(DP[i][j], DP[i]
                                           [j + 1], DP[i + 1][j]) + 1
                    max_side = max(max_side, DP[i + 1][j + 1])
        print(DP)
        return max_side**2


# @lc code=end
