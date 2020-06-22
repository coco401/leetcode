#
# @lc app=leetcode.cn id=240 lang=python3
#
# [240] 搜索二维矩阵 II
#
# https://leetcode-cn.com/problems/search-a-2d-matrix-ii/description/
#
# algorithms
# Medium (40.67%)
# Likes:    341
# Dislikes: 0
# Total Accepted:    61.8K
# Total Submissions: 151.2K
# Testcase Example:  '[[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]]\n5'
#
# 编写一个高效的算法来搜索 m x n 矩阵 matrix 中的一个目标值 target。该矩阵具有以下特性：
#
#
# 每行的元素从左到右升序排列。
# 每列的元素从上到下升序排列。
#
#
# 示例:
#
# 现有矩阵 matrix 如下：
#
# [
# ⁠ [1,   4,  7, 11, 15],
# ⁠ [2,   5,  8, 12, 19],
# ⁠ [3,   6,  9, 16, 22],
# ⁠ [10, 13, 14, 17, 24],
# ⁠ [18, 21, 23, 26, 30]
# ]
#
#
# 给定 target = 5，返回 true。
#
# 给定 target = 20，返回 false。
#
#

# @lc code=start
class Solution:
    def searchMatrix(self, matrix, target):
        M = len(matrix)
        if M == 0:
            return False
        N = len(matrix[0])
        
        row, col = 0, N - 1
        while row < M and col >= 0:
            if matrix[row][col] == target:
                return True
            elif matrix[row][col] < target:
                row += 1
            else:
                col -= 1 
        return False
            



    #好像不需要二分法。。。
    # def searchMatrix(self, matrix, target):
    #     """
    #     :type matrix: List[List[int]]
    #     :type target: int
    #     :rtype: bool
    #     """
    #     M = len(matrix)-1
    #     if M < 0:
    #         return False 
    #     N = len(matrix[0])-1
    #     if N < 0:
    #         return False
    #     if target < matrix[0][0] or target > matrix[M][N]:
    #         return False
    #     res, index= self.binserach(matrix[0],target)
    #     print((res,index))
    #     if res:
    #         return True

    #     matrix = matrix[1:]
    #     newmatrix = list(map(list, zip(*matrix)))
    #     newmatrix = newmatrix[:index]

    #     return self.searchMatrix(newmatrix, target)
        

    # def binserach(self, array, target):
    #     left, right = 0, len(array) - 1
    #     while left + 1 < right:
    #         mid = (left + right) // 2
    #         if array[mid] < target:
    #             left = mid
    #         else:
    #             right = mid
    #     if array[left] < target < array[right]:
    #         return (False, right)
    #     if target == array[left] or target == array[right]:
    #         return (True, left) if target == array[left] else (True, right)
    #     if target > array[right]:
    #         return (False, right + 1)
    #     if target < array[left]:
    #         return (False, left)

# @lc code=end
