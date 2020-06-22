#
# @lc app=leetcode.cn id=136 lang=python3
#
# [136] 只出现一次的数字
#
# https://leetcode-cn.com/problems/single-number/description/
#
# algorithms
# Easy (68.74%)
# Likes:    1335
# Dislikes: 0
# Total Accepted:    227.1K
# Total Submissions: 329.6K
# Testcase Example:  '[2,2,1]'
#
# 给定一个非空整数数组，除了某个元素只出现一次以外，其余每个元素均出现两次。找出那个只出现了一次的元素。
# 
# 说明：
# 
# 你的算法应该具有线性时间复杂度。 你可以不使用额外空间来实现吗？
# 
# 示例 1:
# 
# 输入: [2,2,1]
# 输出: 1
# 
# 
# 示例 2:
# 
# 输入: [4,1,2,1,2]
# 输出: 4
# 
#

# @lc code=start
class Solution:
    from collections import defaultdict, Counter

    def singleNumber(self, nums: List[int]) -> int:
        c = Counter(nums)
        for key, value in c.items():
            if value == 1:
                return key

    def singleNumber(self, nums: List[int]) -> int:
        """
        Math based
        O(1) memory
        """
        total_sum = sum(nums)
        uniq_sum = sum(set(nums))

        return (2 * uniq_sum - total_sum)
# @lc code=end

