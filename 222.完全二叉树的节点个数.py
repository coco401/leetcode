#
# @lc app=leetcode.cn id=222 lang=python3
#
# [222] 完全二叉树的节点个数
#
# https://leetcode-cn.com/problems/count-complete-tree-nodes/description/
#
# algorithms
# Medium (70.39%)
# Likes:    178
# Dislikes: 0
# Total Accepted:    23.7K
# Total Submissions: 33.7K
# Testcase Example:  '[1,2,3,4,5,6]'
#
# 给出一个完全二叉树，求出该树的节点个数。
# 
# 说明：
# 
# 
# 完全二叉树的定义如下：在完全二叉树中，除了最底层节点可能没填满外，其余每层节点数都达到最大值，并且最下面一层的节点都集中在该层最左边的若干位置。若最底层为第
# h 层，则该层包含 1~ 2^h 个节点。
# 
# 示例:
# 
# 输入: 
# ⁠   1
# ⁠  / \
# ⁠ 2   3
# ⁠/ \  /
# 4  5 6
# 
# 输出: 6
# 
#

# @lc code=start
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# BFS遍历二叉树
class Solution:
    def countNodes(self, root: TreeNode) -> int:
        from collections import deque
        res = 0
        if not root:
            return res
        q = deque([root])
        while q:
            node = q.popleft()
            res += 1
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
        return res

# 递归DFS
class Solution:
    def countNodes(self, root: TreeNode) -> int:
        if root == None:
            return 0
        return 1 + self.countNodes(root.left) + self.countNodes(root.right)

# 好方法
class Solution:
    def countNodes(self, root: TreeNode) -> int:
        lh = 0
        node = root;
        while(node != None):
            lh += 1
            node = node.left
        rh = 0
        node = root
        while(node != None):
            rh += 1
            node = node.right
        if lh == rh:
            return pow(2, lh) - 1
        return 1 + self.countNodes(root.left) + self.countNodes(root.right)

# @lc code=end

