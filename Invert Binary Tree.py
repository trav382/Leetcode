# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def invertTree(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: Optional[TreeNode]
        """
        if root == None:
            return None
        
        left_temp = root.left
        root.left = root.right
        root.right = left_temp

        root.left = self.invertTree(root.left)
        root.right = self.invertTree(root.right)
        return root


#This works because Python evaluates the right-hand side fully before assigning to the left-hand side. So both recursive calls happen with the original children.
#root.left, root.right = self.invertTree(root.right), self.invertTree(root.left)
