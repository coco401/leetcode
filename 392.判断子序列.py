#
# @lc app=leetcode.cn id=392 lang=python3
#
# [392] 判断子序列
#


# @lc code=start
# 时间复杂度O(n)
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        i, j = 0, 0
        if not s:
            return True
        for i in range(len(t)):
            if t[i] == s[j]:
                j += 1
            if j == len(s):
                return True
        return False


# @lc code=end
