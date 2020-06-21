#
# @lc app=leetcode.cn id=59 lang=python3
#
# [59] 螺旋矩阵 II
#
# https://leetcode-cn.com/problems/spiral-matrix-ii/description/
#
# algorithms
# Medium (77.43%)
# Likes:    192
# Dislikes: 0
# Total Accepted:    36.1K
# Total Submissions: 46.6K
# Testcase Example:  '3'
#
# 给定一个正整数 n，生成一个包含 1 到 n^2 所有元素，且元素按顺时针顺序螺旋排列的正方形矩阵。
#
# 示例:
#
# 输入: 3
# 输出:
# [
# ⁠[ 1, 2, 3 ],
# ⁠[ 8, 9, 4 ],
# ⁠[ 7, 6, 5 ]
# ]
#
#


# @lc code=start
class Solution:
    def generateMatrix(self, n):

        l, r, t, b = 0, n - 1, 0, n - 1
        mat = [[0 for _ in range(n)] for _ in range(n)]
        num = 1
        tar = n * n
        while num <= tar:
            for i in range(l, r + 1):
                mat[t][i] = num
                num += 1
            t += 1
            for i in range(t, b + 1):
                mat[i][r] = num
                num += 1
            r -= 1
            for i in range(r, l - 1, -1):
                mat[b][i] = num
                num += 1
            b -= 1
            for i in range(b, t - 1, -1):
                mat[i][l] = num
                num += 1
            l += 1

        return mat


# @lc code=end
