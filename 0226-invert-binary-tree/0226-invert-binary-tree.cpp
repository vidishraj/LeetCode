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
    TreeNode* invertTree(TreeNode* root) {
     //do level order traversal and then reverse the container
        //can i do it recurssively?
        if( root==NULL){
            return NULL;
        }
        TreeNode* left=NULL;
        TreeNode* right=NULL;
        if( root->left){
            left=root->left;
        }
        if( root->right){
            right=root->right;
        }
        root->left=right;
        root->right=left;
        invertTree(root->left);
        invertTree(root->right);
        return root;
    }
};