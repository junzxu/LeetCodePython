# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param preorder, a list of integers
    # @param inorder, a list of integers
    # @return a tree node
    def buildTree(self, preorder, inorder):
        if preorder is None or len(preorder) == 0 or inorder is None or len(inorder)==0:
            return None
        root_val = preorder[0]
        root = TreeNode(root_val)
        index = inorder.index(root_val)
        inorder_left = inorder[0:index]
        inorder_right = inorder[index+1:]
        preorder_left = preorder[1: index+1]
        preorder_right = preorder[index+1:]
        
        root.left = self.buildTree(preorder_left, inorder_left)
        root.right = self.buildTree(preorder_right, inorder_right)
        
        return root