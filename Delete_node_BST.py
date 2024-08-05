'''
Delete a node in BST
Given a Binary Search Tree and a node value x. Delete the node with the given value x from the BST. If no node with value x exists,
then do not make any change. Return the root of the BST after deleting the node with value x. Do not make any update if there's no node with value x present in the BST.

Note: The generated output will be the inorder traversal of the modified tree.

Examples :

Input:
      2
    /   \
   1     3
x = 12
Output: 1 2 3
Explanation: In the given input there is no node with value 12 , so the tree will remain same.
'''
def deleteNode(root, X):
    def min_func(root):
        while root.left!=None:
            root=root.left
        return root.data
    def delete_func(root,X):
        if root==None:
            return None
            
        if root.data>X:
            root.left=delete_func(root.left,X)
        elif root.data<X:
            root.right=delete_func(root.right,X)
        else:
            if root.left==None:
                return root.right
            elif root.right==None:
                return root.left
            else:
                min_value=min_func(root.right)
                root.data=min_value
                root.right=delete_func(root.right,min_value)
                
        return root
        
    return delete_func(root,X)

