# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.depth = 0
        
        def find_depth(root: Optional[TreeNode]) -> int:
            if root is None:
                return 0

            left = find_depth(root.left)
            right = find_depth(root.right)

            self.depth = max(self.depth, left + right)

            return max(left, right) + 1

        find_depth(root)

        return self.depth