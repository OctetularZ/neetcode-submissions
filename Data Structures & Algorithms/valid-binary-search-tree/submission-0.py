# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def dfs(node, left, right):
            if not node:
                return True
            
            if not left < node.val < right:
                return False
            
            return dfs(node.left, left, node.val) and dfs(node.right, node.val, right)
            


        return dfs(root, float('-inf'), float('inf'))

# Returning each nodes value
# Compare at each recursively called function
# Node.right must be more than current nodes value
# Node.left must be less than current nodes value
# Two return values, True/False and that nodes values

# Fails: if root is 2, right is 3, then left of 3 is 1.
# 1 is less than 3 but less than 2 as well. Invalid BST.
# Above solution doesn't take into consideration earlier nodes

# Thinking of using some sort of min/max to compare each node with
# Instead, we can take the max and min at each stage
# Pass max to right, min to left
# Any right node: Bigger than min and more than parent
# Any left node: Smaller than max and less than parent
# Update min, max
# ???

# Looked at solution, I was almost right, just didn't know how what do when going left on a right subtree
# We pass down left and right and update the ranges each time we left and right starting with -inf and inf
# As we go left, number must be between -inf and previous node
# As we go right, number must be between previous node and inf
# That way, when we go left on a right subtree, we pass prev node and current node
# So it'll have to be between prev node and current node
