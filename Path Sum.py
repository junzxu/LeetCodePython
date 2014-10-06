# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param root, a tree node
    # @param sum, an integer
    # @return a boolean
    def hasPathSum(self, root, sum):
        if root == None:
            return False
        new_sum = sum - root.val
        if new_sum == 0 and root.left == None and root.right == None:
            #if we are at a leaf node and the sum equals target
            return True
        left = self.hasPathSum(root.left, new_sum) #find path in left node
        right = self.hasPathSum(root.right, new_sum) #find path in right node
        
        if left or right:
            #if we find at left or right node
            return True
        else:
            return False