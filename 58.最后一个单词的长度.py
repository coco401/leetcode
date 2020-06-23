#
# @lc app=leetcode.cn id=58 lang=python3
#
# [58] 最后一个单词的长度
#

# @lc code=start
class Solution:
    def lengthOfLastWord(self, s: str) -> int:

        words = s.split()

        return len(words[-1]) if words else 0
        
# @lc code=end

