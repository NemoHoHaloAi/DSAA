# 给你一个二叉树，请你返回其按 层序遍历 得到的节点值。 （即逐层地，从左到右访问所有节点）。
# 
#  
# 
# 示例：
# 二叉树：[3,9,20,null,null,15,7],
# 
#     3
#    / \
#   9  20
#     /  \
#    15   7
# 返回其层次遍历结果：
# 
# [
#   [3],
#   [9,20],
#   [15,7]
# ]
# 
# 链接：https://leetcode-cn.com/problems/binary-tree-level-order-traversal

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    levelArray = []

    def getLevel(self, root, lvl):
        if not root:
            return
        if len(self.levelArray) <= lvl:
            self.levelArray.append([])
        self.levelArray[lvl].append(root.val)
        self.getLevel(root.left, lvl+1)
        self.getLevel(root.right, lvl+1)
    
    def levelOrder(self, root):
        if not root:
            return []
        if not root.left and not root.right:
            return [[root.val]]
        
        self.levelArray = []
        self.getLevel(root, 0)
        return self.levelArray