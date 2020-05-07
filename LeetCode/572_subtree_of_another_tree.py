# 给定两个非空二叉树 s 和 t，检验 s 中是否包含和 t 具有相同结构和节点值的子树。s 的一个子树包括 s 的一个节点和这个节点的所有子孙。s 也可以看做它自身的一棵子树。
# 
# 示例 1:
# 给定的树 s:
# 
#      3
#     / \
#    4   5
#   / \
#  1   2
# 给定的树 t：
# 
#    4 
#   / \
#  1   2
# 返回 true，因为 t 与 s 的一个子树拥有相同的结构和节点值。
# 
# 链接：https://leetcode-cn.com/problems/subtree-of-another-tree

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def isSubtree(self, s, t):
        """
        :type s: TreeNode
        :type t: TreeNode
        :rtype: bool
        """
        if not s and not t:
            return True
        if not s or not t:
            return False
        # 子树的三种可能s==t，s的左子树包含t，s的右子树包含t
        return self.isSameTree(s, t) or self.isSubtree(s.left, t) or self.isSubtree(s.right, t)
        
    def isSameTree(self, s, t):
        if not s and not t:
            return True
        if not s or not t:
            return False
        # 树的一致性判断，判断当前点以及左右子树即可
        return s.val == t.val and self.isSameTree(s.left, t.left) and self.isSameTree(s.right, t.right)

s = TreeNode(3)
s.left = TreeNode(4)
s.right = TreeNode(5)
s.left.left = TreeNode(1)
s.left.right = TreeNode(2)

t = TreeNode(4)
t.left = TreeNode(1)
t.right = TreeNode(2)

included = Solution().isSubtree(s, t)
print(included)

s = TreeNode(3)
s.left = TreeNode(4)
s.right = TreeNode(5)
s.left.left = TreeNode(1)
s.left.right = TreeNode(2)
s.left.right.left = TreeNode(0)

t = TreeNode(4)
t.left = TreeNode(1)
t.right = TreeNode(2)

included = Solution().isSubtree(s, t)
print(included)