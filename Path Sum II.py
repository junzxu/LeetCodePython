# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param root, a tree node
    # @param sum, an integer
    # @return a list of lists of integers
    def pathSum(self, root, sum):
        result = []
        if root == None:
            return []
        new_sum = sum - root.val
        if new_sum == 0 and root.left == None and root.right == None:
            return [[root.val]]
        left = self.pathSum(root.left, new_sum)
        right = self.pathSum(root.right, new_sum)
        
        #back tracking
        for li in left:
            new = [root.val] + li
            result.append(new)
        for li in right:
            new = [root.val] + li
            result.append(new)
        
        return result