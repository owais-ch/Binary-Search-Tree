'''

Given a Binary Tree, write a function to check whether the given Binary Tree is Complete Binary Tree or not. A complete binary tree is a binary tree in which every level,
except possibly the last, is completely filled, and all nodes should be as much close to left as possible.


Example 1:
Input:
       1
      / \
     2   3
Output:
Complete Binary Tree
'''

class Solution():
    def isCompleteBT(self, root):
        def traversal(root,level,arr):
            if root==None:
                arr.append(None)
                return None
                
            if level==0:
                arr.append(root.data)
            else:
                traversal(root.left,level-1,arr)
                traversal(root.right,level-1,arr)
                
        
        
        def height(root):
            if root==None:
                return 0
                
            lh=height(root.left)
            rh=height(root.right)
            
            return max(lh,rh)+1
            
        tall=height(root)
        
        arr=[]
        
        for i in range(tall):
            traversal(root,i,arr)
            if i<tall-1:
                if None in arr:
                    return False
            else:
                
                length2=len(arr)
                for j in range(1,length2):
                    
                    if arr[j-1]==None and arr[j]!=None:
                        #print(arr[0],arr[1])
                        return False
                
            arr=[]
            
        return True
            
