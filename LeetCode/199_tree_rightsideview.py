# 二叉树的右侧视图打印
# 给定一棵二叉树，想象自己站在它的右侧，按照从顶部到底部的顺序，返回从右侧所能看到的节点值。
# 
# 示例:
# 
# 输入: [1,2,3,null,5,null,4]
# 输出: [1, 3, 4]
# 解释:
# 
#    1            <---
#  /   \
# 2     3         <---
#  \     \
#   5     4       <---

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    levels = []
    def level_count(self, nodes, level):
        # print(level, nodes)
        if not nodes or len(nodes) <= 0:
            return
        self.levels.append([node.val for node in nodes])
        tmp = []
        for node in nodes:
            if node.left:
                tmp.append(node.left)
            if node.right:
                tmp.append(node.right)
        nodes = tmp
        self.level_count(nodes, level+1)

    def rightSideView(self, root):
        '''
        题目链接：https://leetcode-cn.com/problems/binary-tree-right-side-view/
        解题思路：收集每一层的节点值，取最后一个返回
        '''
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return []
        if not root.left and not root.right:
            return [root.val]
        self.levels = []
        self.level_count([root], 0)
        return [level[-1] for level in self.levels]

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = None
root.left.right = TreeNode(5)
root.right.left = None
root.right.right = TreeNode(4)

print(Solution().rightSideView(root))