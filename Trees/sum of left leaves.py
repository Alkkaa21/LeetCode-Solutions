# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        
        
        def leaf(node):
            if node is None:
                return 0
            
            if node.left and node.left.left is None and node.left.right is None:
                leftsum=node.left.val
            else:
                leftsum=leaf(node.left)

            rightsum=leaf(node.right)
            return leftsum+rightsum
        return leaf(root)
            