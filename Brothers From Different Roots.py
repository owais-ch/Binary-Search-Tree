'''Given two BSTs containing N1 and N2 distinct nodes respectively and given a value x. Your task is to complete the function countPairs(),
that returns the count of all pairs from both the BSTs whose sum is equal to x.

Example 1:

Input:
BST1:
       5
     /   \
    3     7
   / \   / \
  2   4 6   8

BST2:
       10
     /    \
    6      15
   / \    /  \
  3   8  11   18

x = 16
Output:
3'''

class Solution:
    def countPairs(self, root1, root2, x): 
        def traversal(root,arr):
            if root==None:
                return None
            
            if root.left:
                traversal(root.left,arr)
            
            arr.append(root.data)
                
            if root.right:
                traversal(root.right,arr)
                
        arr1,arr2=[],[]
        
        traversal(root1,arr1)
        traversal(root2,arr2)
        
        count=0
        
        length1,length2=len(arr1),len(arr2)
        
        
        dict2={i:1 for i in arr2}
        
        for i in range(length1):
            if x-arr1[i] in dict2:
                count+=1
            
                
        return count
