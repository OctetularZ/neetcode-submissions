# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if not root:
            return None

        if key < root.val:
            root.left = self.deleteNode(root.left, key)

        elif key > root.val:
            root.right = self.deleteNode(root.right, key)

        else:
            # no left child
            if not root.left:
                return root.right

            # no right child
            if not root.right:
                return root.left

            # two children
            successor = root.right

            while successor.left:
                successor = successor.left

            root.val = successor.val

            root.right = self.deleteNode(root.right, successor.val)

        return root
            


# 1) Search for node to remove

# 2) Delete node if it's found
    # If not found, return root

# If you have to remove the root, or a child with two other children:
    # Find inorder successor (smallest node in right subtree)
    # Copy value into node being deleted
    # Delete successor node
