#
# @lc app=leetcode.cn id=1044 lang=python3
#
# [1044] 最长重复子串
#
# https://leetcode-cn.com/problems/longest-duplicate-substring/description/
#
# algorithms
# Hard (18.29%)
# Likes:    50
# Dislikes: 0
# Total Accepted:    2.1K
# Total Submissions: 10.8K
# Testcase Example:  '"banana"'
#
# 给出一个字符串 S，考虑其所有重复子串（S 的连续子串，出现两次或多次，可能会有重叠）。
#
# 返回任何具有最长可能长度的重复子串。（如果 S 不含重复子串，那么答案为 ""。）
#
#
#
# 示例 1：
#
# 输入："banana"
# 输出："ana"
#
#
# 示例 2：
#
# 输入："abcd"
# 输出：""
#
#
#
#
# 提示：
#
#
# 2 <= S.length <= 10^5
# S 由小写英文字母组成。
#
#
#

# @lc code=start
class Solution:

    def longestDupSubstring(self, S: str) -> str:
        n = len(S)
        left, right = 0, n-1
        while left < right - 1:
            mid = (left + right) // 2
            isFound, _ = self.RabinKarp(mid, S) 
            if isFound:
                left = mid 
            else:
                right = mid
        isFound, res = self.RabinKarp(right, S)
        if isFound:
            return res
        isFound, res = self.RabinKarp(left, S)
        if isFound:
            return res
        return ''

    def RabinKarp(self, L, S):
        '''
        input:
        -L为猜测的长度
        -S为目标字符串
        output:
        (真假值,字符串)
        '''
        a = 26
        n = len(S)
        h = 0
        nums = [ord(S[i]) - ord('a') for i in range(n)]
        for i in range(L):
            h = (h * a + nums[i]) % 2**32
        
        aL = pow(a, L, 2**32)
        seen = {h}
        for start in range(1, n - L + 1):
            # compute rolling hash in O(1) time
            h = (h * a - nums[start - 1] * aL + nums[start + L - 1]) % 2**32
            if h in seen:
                return (True, S[start: start+L])
            else:
                seen.add(h)
        return (False, '')
# @lc code=end
