class Solution {
public:
    vector<TreeNode*> findDuplicateSubtrees(TreeNode* root) {
        unordered_map<string, int> counter;
        vector<TreeNode*> result;
        dfs(root, counter, result);
        return result;
    }
    
private:
    string dfs(TreeNode* node, unordered_map<string, int>& counter, vector<TreeNode*>& result) {
        if (!node) {
            return "#";
        }
        string left = dfs(node->left, counter, result);
        string right = dfs(node->right, counter, result);
        string tree = to_string(node->val) + "," + left + "," + right;
        if (++counter[tree] == 2) {
            result.push_back(node);
        }
        return tree;
    }
};
