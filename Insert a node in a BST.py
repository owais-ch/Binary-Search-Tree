'''Given a BST and a key K. If K is not present in the BST, Insert a new Node with a value equal to K into the BST. 
Note: If K is already present in the BST, don't modify the BST.


Example 1:

Input:
     2
   /   \
  1     3
K = 4
Output: 1 2 3 4
Explanation: After inserting the node 4
Inorder traversal will be 1 2 3 4.'''


def insert(root, Key):
    if root.data==None:
        root.data=Key
        return
    elif root.data==Key:
        return
    
    if root.data>Key:
        if root.left:
            insert(root.left,Key)
        else:
            root.left=Node(Key)
    elif root.data<Key:
        if root.right:
            insert(root.right,Key)
        else:
            root.right=Node(Key) 
