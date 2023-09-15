# Given a BST and a key K. 
# If K is not present in the BST, Insert a new Node with a value equal to K into the BST. 
# If K is already present in the BST, don't modify the BST.

class Solution:
    # Function to insert a node in a BST.
    def insert(self, root, Key):
        # If the root is None, create a new node and return it as the new root.
        if root is None:
            return Node(Key)
        
        # If the Key is less than the current node's value, insert it in the left subtree.
        if Key < root.data:
            root.left = self.insert(root.left, Key)
        # If the Key is greater than the current node's value, insert it in the right subtree.
        elif Key > root.data:
            root.right = self.insert(root.right, Key)
        
        # Return the modified root node.
        return root

