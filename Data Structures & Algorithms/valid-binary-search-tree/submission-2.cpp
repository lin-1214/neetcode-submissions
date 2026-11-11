/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */

class Solution {
public:
    bool isValidBST(TreeNode* root) {
        if (!root) return true;
        return isValidNode(root, -1001, 1001);
    }

private:
    bool isValidNode(TreeNode* n, int lb, int ub) {
        if (!n) return true;
        if (n->val >= ub || n->val <= lb) return false;

        return (isValidNode(n->left, lb, n->val) && isValidNode(n->right, n->val, ub));
        
    }
};
