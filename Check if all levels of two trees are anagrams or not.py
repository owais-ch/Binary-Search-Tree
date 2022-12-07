'''Given two binary trees with same number of nodes, the task is to check if each of their levels are anagrams of each other or not. 
Note: All nodes of a tree should be unique.

Example 1:

Input:

Output: 1
Explanation: 
Tree 1:
Level 0 : 1
Level 1 : 3, 2
Level 2 : 5, 4

Tree 2:
Level 0 : 1
Level 1 : 2, 3
Level 2 : 4, 5

As we can clearly see all the levels of above two binary trees 
are anagrams of each other, hence return true.
'''

class Solution:
    def areAnagrams(self, node1 : Optional['Node'], node2 : Optional['Node']) -> bool:
        def height(root):
            if root==None:
                return 0
            
            lh=height(root.left)
            rh=height(root.right)
            
            return max(lh,rh)+1
            
        tall1=height(node1)
        tall2=height(node2)
        
        if tall1!=tall2:
            return False
            
        def traversal(root,level,arr):
            if root==None:
                return None
                
            if level==0:
                arr.append(root.data)
            else:
                traversal(root.left,level-1,arr)
                traversal(root.right,level-1,arr)
                
        arr1=[]
        arr2=[]
        
        for i in range(tall1):
            traversal(node1,i,arr1)
            traversal(node2,i,arr2)
            
            if sorted(arr1)!=sorted(arr2):
                return False
                
            arr1,arr2=[],[]
            
        return True
