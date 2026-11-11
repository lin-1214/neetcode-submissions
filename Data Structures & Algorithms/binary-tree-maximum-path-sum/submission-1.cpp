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
    int maxPathSum(TreeNode* root) {
        int dummy = dfs(root);

        return res;
    }

private:
    int res = INT_MIN;
    int dfs(TreeNode* n) {
        if (!n) return 0;
        int left = dfs(n->left);
        int right = dfs(n->right);

        int leftMax = std::max(0, left);
        int rightMax = std::max(0, right);

        res = std::max(res, n->val + leftMax + rightMax);

        return (n->val + max(leftMax, rightMax));
    }
};
