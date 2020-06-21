#
# @lc app=leetcode.cn id=46 lang=python3
#
# [46] 全排列
#
# https://leetcode-cn.com/problems/permutations/description/
#
# algorithms
# Medium (76.12%)
# Likes:    752
# Dislikes: 0
# Total Accepted:    141.6K
# Total Submissions: 185.7K
# Testcase Example:  '[1,2,3]'
#
# 给定一个 没有重复 数字的序列，返回其所有可能的全排列。
#
# 示例:
#
# 输入: [1,2,3]
# 输出:
# [
# ⁠ [1,2,3],
# ⁠ [1,3,2],
# ⁠ [2,1,3],
# ⁠ [2,3,1],
# ⁠ [3,1,2],
# ⁠ [3,2,1]
# ]
#
#

# @lc code=start
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        self.DFS(nums, [], res)
        return res

    def DFS(self, nums, path, res):
        if not nums:
            res.append(path)
            return
        for i in range(len(nums)):
            self.DFS(nums[:i] + nums[i+1:], path + [nums[i]], res)
# @lc code=end
