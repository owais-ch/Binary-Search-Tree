'''
Normal BST to Balanced BST

Given a Binary Search Tree, modify the given BST such that it is balanced and has minimum possible height. Return the balanced BST.

Example1:

Input:
       30
      /
     20
    /
   10
Output:
     20
   /   \
 10     30
'''

class Solution:
    def buildBalancedTree(self,root):
        def traversal(root):
            if root==None:
                return None
                
            if root.left:
                traversal(root.left)
            
            list1.append(root.data)
            
            if root.right:
                traversal(root.right)
                
        def buildBST(arr,start,end):
            if start>end:
                return None
            
            mid=(start+end)//2
            node=Node(arr[mid])
            
            node.left=buildBST(arr,start,mid-1)
            node.right=buildBST(arr,mid+1,end)
            
            return node
        
        list1=[]
        
        traversal(root)
        
        length=len(list1)
        
        return buildBST(list1,0,length-1)
