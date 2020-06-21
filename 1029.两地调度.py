#
# @lc app=leetcode.cn id=1029 lang=python3
#
# [1029] 两地调度
#


# @lc code=start
class Solution:
    def twoCitySchedCost(self, costs):

        costs.sort(key=lambda x: x[0] - x[1])

        res = 0
        res += sum([i[0] for i in costs[:len(costs) // 2]])
        res += sum([i[1] for i in costs[len(costs) // 2:]])

        return res


# @lc code=end
