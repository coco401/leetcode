#
# @lc app=leetcode.cn id=54 lang=python3
#
# [54] 螺旋矩阵
#


# @lc code=start
class Solution:
    def spiralOrder(self, matrix):
        return matrix and list(matrix.pop(0)) + self.spiralOrder(list(zip(*matrix))[::-1])

        # res = []
        # col = len(matrix)
        # row = len(matrix[0])
        # viewed = [[False for _ in range(row)] for _ in range(col)]
        # i, j = 0, 0
        # N = col * row
        
        # while N > 1:    
        #     while j < row - 1 and viewed[i][j + 1] == False:
        #         res.append(matrix[i][j])
        #         viewed[i][j] = True
        #         j += 1
        #         N -= 1

        #     while i < col - 1 and viewed[i + 1][j] == False:
        #         res.append(matrix[i][j])
        #         viewed[i][j] = True
        #         i += 1
        #         N -= 1

        #     while j > 0 and viewed[i][j - 1] == False:
        #         res.append(matrix[i][j])
        #         viewed[i][j] = True
        #         j -= 1
        #         N -= 1

        #     while i > 0 and viewed[i - 1][j] == False:
        #         res.append(matrix[i][j])
        #         viewed[i][j] = True
        #         i -= 1
        #         N -= 1
        # res.append(matrix[i][j])
        # return res
            
s = Solution()
s.spiralOrder([[1,2,3],[4,5,6],[7,8,9]])           


# @lc code=end
