# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param root, a tree node
    # @return nothing, do it in place
    def flatten(self, root):
        pre = self.pre_order(root)
        node = root
        for i in range(1,len(pre)):
            node.left = None
            node.right = pre[i]
            node = pre[i]
    
    
    def pre_order(self, root):
        #return pre order traverse list
        if root is None:
            return []
        return [root] + self.pre_order(root.left) + self.pre_order(root.right)