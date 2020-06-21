#
# @lc app=leetcode.cn id=547 lang=python3
#
# [547] 朋友圈
#


# @lc code=start
class UnionFind():
    def __init__(self, n):
        self.father = {i: i for i in range(n)}
        self.count = n

    def Union(self, a, b):
        fa = self.find(a)
        fb = self.find(b)
        if fa != fb:
            self.father[fb] = fa
            self.count -= 1

    def find(self, aa):
        j = aa
        while j != self.father[j]:  #find big brother
            j = self.father[j]

        while aa != j:
            fx = self.father[aa]
            self.father[aa] = j
            aa = fx
        return j


class Solution:
    def findCircleNum(self, M: List[List[int]]) -> int:
        n = len(M)
        uf = UnionFind(n)
        for i in range(n):
            for j in range(n):
                if M[i][j] == 1:
                    uf.Union(i, j)
        return uf.count


# @lc code=end
