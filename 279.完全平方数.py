#
# @lc app=leetcode.cn id=279 lang=python3
#
# [279] 完全平方数
#
# https://leetcode-cn.com/problems/perfect-squares/description/
#
# algorithms
# Medium (56.53%)
# Likes:    463
# Dislikes: 0
# Total Accepted:    66.7K
# Total Submissions: 118K
# Testcase Example:  '12'
#
# 给定正整数 n，找到若干个完全平方数（比如 1, 4, 9, 16, ...）使得它们的和等于 n。你需要让组成和的完全平方数的个数最少。
#
# 示例 1:
#
# 输入: n = 12
# 输出: 3
# 解释: 12 = 4 + 4 + 4.
#
# 示例 2:
#
# 输入: n = 13
# 输出: 2
# 解释: 13 = 4 + 9.
#
#

# @lc code=start

# DP ， python Time Limit Exceeded

class Solution:
    def __init__(self):
        super().__init__()
        self.hashmap = {0: 0, 1: 1, 2: 2, 3: 3}

    # def numSquares(self, n: int) -> int:
    #     # 如果保存了则直接返回
    #     if n in self.hashmap:
    #         return self.hashmap[n]

    #     count = n
    #     i = 1
    #     while i * i <= n:
    #         count = min(count, self.numSquares(n-i*i) + 1)
    #         i += 1
    #     self.hashmap[n] = count
    #     return count

    def numSquares(self, n: int) -> int:
        dp = [0] * (n+1)
        for x in range(1, n+1):
            min_val = x
            i = 1
            while i*i <= x:
                min_val = min(min_val, 1 + dp[x-i*i])
                i += 1
            dp[x] = min_val
        return dp[n]
# @lc code=end
