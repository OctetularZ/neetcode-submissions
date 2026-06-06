# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def dfs(node, max_node):
            if not node:
                return 0
            
            if node.val >= max_node:
                res = 1
            else:
                res = 0
            
            max_node = max(max_node, node.val)

            res += dfs(node.left, max_node)
            res += dfs(node.right, max_node)

            return res


        return dfs(root, float('-inf'))
        

# Hold current maximum node as we traverse down tree (dfs)
# Complete search for each node in the tree
# Root node is always a good node as there is nothing before it, so we always at least return 1
# At each node, check if max is greater than current node, if not, then current node is a good node.