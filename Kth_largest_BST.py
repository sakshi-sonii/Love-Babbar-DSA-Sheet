# Given a Binary Search Tree. 
# task is to complete the function which will return the Kth largest element 
# without doing any modification in Binary Search Tree

# class Node:
#     def __init__(self, val):
#         self.data = val
#         self.left = None
#         self.right = None

# return the Kth largest element in the given BST rooted at 'root'
class Solution:
    def kthLargest(self, root, k):
        def reverse_inorder_traversal(node):
            nonlocal k, result
            if not node or k == 0:
                return

            # Recur on the right subtree
            reverse_inorder_traversal(node.right)

            # Decrement k for each visited node
            k -= 1

            # If k reaches 0, we have found the Kth largest element
            if k == 0:
                result = node.data
                return

            # Recur on the left subtree
            reverse_inorder_traversal(node.left)

        k = k
        result = None
        reverse_inorder_traversal(root)

        return result