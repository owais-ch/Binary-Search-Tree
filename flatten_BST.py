'''
Flatten BST to sorted list (GFG)
You are given a Binary Search Tree (BST) with n nodes, each node has a distinct value assigned to it. The goal is to flatten the tree such that, the left child of each element points to nothing (NULL), and the right child points to the next element in the sorted list of elements of the BST (look at the examples for clarity). You must accomplish this without using any extra storage, except for recursive calls, which are allowed.

Note: If your BST does have a left child, then the system will print a -1 and will skip it, resulting in an incorrect solution.

Example 1:

Input:
          5
        /    \
       3      7
      /  \    /   \
     2   4  6     8
Output: 2 3 4 5 6 7 8
Explanation: 
After flattening, the tree looks
like this
    2
     \
      3
       \
        4
         \
          5
           \
            6
             \
              7
               \
                8
Here, left of each node points
to NULL and right contains the
next node.
'''

import sys
sys.setrecursionlimit(10000)

class Solution:
    def flattenBST(self, root):
        def traversal(root):
            if root==None:
                return None
                
            if root.left:
                traversal(root.left)
                
            arr.append(root.data)
            
            if root.right:
                traversal(root.right)
                
        arr=[]
        
        traversal(root)
        length=len(arr)
        
        def buildBST(arr,start):
            if start>=length:
                return 
            
            root=Node(arr[start])
            start+=1
            root.right=buildBST(arr,start)
            
            return root
            
        return buildBST(arr,0)
