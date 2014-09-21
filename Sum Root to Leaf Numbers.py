# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param root, a tree node
    # @return an integer
    def sumNumbers(self, root):
        numbers = self.findNumbers(root)
        real_numbers = [int(number) for number in numbers]
        return sum(real_numbers)
    
    def findNumbers(self,root):
        #recursively find root to leaf strings
        numbers = []
        if root is None:
            return []
        li = self.findNumbers(root.left)
        ri = self.findNumbers(root.right)
        for number in li:
            new_number = str(root.val) + number
            numbers.append(new_number)
        for number in ri:
            new_number = str(root.val) + number
            numbers.append(new_number)
        if len(numbers) == 0:
            numbers.append(str(root.val))
        return numbers
        