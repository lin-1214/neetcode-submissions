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
    int goodNodes(TreeNode* root) {
        return dfs(root, root->val);
    }

private:
    int dfs(TreeNode* n, int max_val) {
        int res = 0;
        if (!n) return res;

        if (n->val >= max_val) res = 1;
        max_val = max(n->val, max_val);
        
        res += dfs(n->left, max_val);
        res += dfs(n->right, max_val);
        
        return res;
    }
};
