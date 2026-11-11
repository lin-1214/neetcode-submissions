# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        lookup = {v: i for i, v in enumerate(inorder)}

        def construct(pre_l, pre_r, in_l, in_r):
            if pre_r < pre_l or in_r < in_l:   # edge case 
                return None

            root_val = preorder[pre_l]
            root = TreeNode(root_val)
            mid = lookup[root_val]
            k = mid - in_l
            root.left = construct(pre_l + 1, pre_l + k, in_l, mid - 1)
            root.right = construct(pre_l + k + 1, pre_r, mid + 1, in_r)

            return root

        return construct(0, len(preorder) - 1, 0, len(inorder) - 1)