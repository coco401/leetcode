#
# @lc app=leetcode.cn id=542 lang=python3
#
# [542] 01 矩阵
#
# https://leetcode-cn.com/problems/01-matrix/description/
#
# algorithms
# Medium (44.76%)
# Likes:    282
# Dislikes: 0
# Total Accepted:    34.3K
# Total Submissions: 76.6K
# Testcase Example:  '[[0,0,0],[0,1,0],[0,0,0]]'
#
# 给定一个由 0 和 1 组成的矩阵，找出每个元素到最近的 0 的距离。
#
# 两个相邻元素间的距离为 1 。
#
# 示例 1:
# 输入:
#
#
# 0 0 0
# 0 1 0
# 0 0 0
#
#
# 输出:
#
#
# 0 0 0
# 0 1 0
# 0 0 0
#
#
# 示例 2:
# 输入:
#
#
# 0 0 0
# 0 1 0
# 1 1 1
#
#
# 输出:
#
#
# 0 0 0
# 0 1 0
# 1 2 1
#
#
# 注意:
#
#
# 给定矩阵的元素个数不超过 10000。
# 给定矩阵中至少有一个元素是 0。
# 矩阵中的元素只在四个方向上相邻: 上、下、左、右。
#
#
#

# @lc code=start
class Solution:
    def updateMatrix(self, matrix: List[List[int]]) -> List[List[int]]:
        if not matrix:
            return []
        M = len(matrix)
        N = len(matrix[0])
        res = [[None for _ in range(N)]for _ in range(M)]

        def BFS(*args):
            from collections import deque
            x, y = args
            d = 0
            queue = deque([(x, y, d)])
            while queue:
                x, y, d = queue.popleft()
                if matrix[x][y] == 0:
                    return d

                #上下左右
                for i, j in [(0, 1), (0, -1), (-1, 0), (1, 0)]:
                    if 0 <= i + x < M and 0 <= j + y < N:
                        queue.append((i + x, j + y, d + 1))
            return d

        for i in range(M):
            for j in range(N):
                if matrix[i][j] == 0:
                    res[i][j] = 0
                else:
                    res[i][j] = BFS(i, j)
        return res

        


# @lc code=end
