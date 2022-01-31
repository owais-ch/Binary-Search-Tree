'''Given a BST, modify it so that all greater values in the given BST are added to every node.

Example 1:

Input:
           50
         /    \
        30    70
      /   \   / \  
     20   40 60  80
Output: 350 330 300 260 210 150 80
Explanation:The tree should be modified to
following:
             260
          /       \
        330      150
       /   \   /     \
    350   300 210    80'''


def modify(root):
    total_sum=0
    
    def traversal(root):
        nonlocal total_sum
        
        total_sum+=root.data
        
        if root.left:
            traversal(root.left)
        if root.right:
            traversal(root.right)
        
        
    def traversal2(root):
        nonlocal total_sum
        if root.left:
            traversal2(root.left)
            
        total_sum=total_sum-root.data
        root.data+=total_sum
        
        if root.right:
            traversal2(root.right)
        
    traversal(root)
    traversal2(root)
    return root
