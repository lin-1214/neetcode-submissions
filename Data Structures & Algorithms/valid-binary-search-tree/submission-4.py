# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def check(node, upper_bound, lower_bound):
            if node is None:
                return True

            if node.val >= upper_bound:
                return False
            
            if node.val <= lower_bound:
                return False

            return check(node.left, node.val, lower_bound) and check(node.right, upper_bound, node.val)

        
        return check(root, float("inf"), float("-inf"))