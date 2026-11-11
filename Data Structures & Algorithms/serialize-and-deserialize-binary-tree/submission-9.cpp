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

class Codec {
public:

    // Encodes a tree to a single string.
    string serialize(TreeNode* root) {
        dfs_ser(root);
        string ret;
        for (int i = 0; i < ser.size(); i++) {
            ret += ser[i];
            if (i != ser.size() - 1) ret += ",";
        }

        return ret;
    }

    // Decodes your encoded data to tree.
    TreeNode* deserialize(string data) {
        vector<string> vals = split(data, ',');
        return dfs_deser(vals);
    }

private:
    vector<string> ser;
    int idx = 0;

    void dfs_ser(TreeNode* n) {
        if (!n) {
            ser.push_back("N");
            return;
        }
        ser.push_back(to_string(n->val));
        dfs_ser(n->left);
        dfs_ser(n->right);
        return;
    }

    TreeNode* dfs_deser(vector<string> data) {
        if (data[idx] == "N") {
            idx++;
            return nullptr;
        }

        TreeNode* node = new TreeNode(stoi(data[idx++]));
        node->left = dfs_deser(data);
        node->right = dfs_deser(data);

        return node;
    }

    vector<string> split(const string &s, char delim) {
        vector<string> elems;
        stringstream ss(s);
        string item;
        while(getline(ss, item, delim)) {
            elems.push_back(item);
        }

        return elems;
    }
};
