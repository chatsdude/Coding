class Solution {
public:
    int ans = 0;
    void solve(TreeNode* root, string cur){
        if(!root->left && !root->right){
            ans += stoi(cur+to_string(root->val),nullptr,2);
            return;
        }
        if(root->left) solve(root->left,cur+to_string(root->val));
        if(root->right) solve(root->right,cur+to_string(root->val));
    }
    int sumRootToLeaf(TreeNode* root) {
        solve(root,"");
        return ans;
        
     }
};
