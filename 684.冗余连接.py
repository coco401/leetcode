#
# @lc app=leetcode.cn id=684 lang=python3
#
# [684] 冗余连接
#


# @lc code=start
class UnionFind:
    def __init__(self, n):
        self.f = {i: i for i in range(1,n+1)}
    
    def Union(self, a, b):
        fa = self.Find(a)
        fb = self.Find(b)
        if fa != fb:
            self.f[fb] = fa
        # else:
        #     return [a, b]

    def Find(self, x):
        j = x
        while j != self.f[j]:
            j = self.f[j]
        while x != j:
            fx = self.f[x]
            self.f[x] = j
            x = fx
        return j


class Solution:
    def findRedundantConnection(self, edges):
        uf = UnionFind(len(edges))
        for edge in edges:
            if uf.Find(edge[0]) == uf.Find(edge[1]):
                res = edge
            uf.Union(edge[0], edge[1])

            
        return res


# @lc code=end
