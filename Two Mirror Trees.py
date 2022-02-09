'''Given a Two Binary Trees, write a function that returns true if one is mirror of other, else returns false.
MirrorTree1            

Example 1:

Input:
T1:     1     T2:     1
      /   \         /   \
     2     3       3     2
Output: 1'''

class Solution:
    def areMirror(self,root1,root2):
        def height(root):
            if root==None:
                return 0
                
            left=height(root.left)
            right=height(root.right)
            
            return max(left,right)+1
        def traversal(root,level,list1):
            if root==None:
                list1.append(None)
                return 
                
            if level==0:
                list1.append(root.data)
            else:
                traversal(root.left,level-1,list1)
                traversal(root.right,level-1,list1)
                
        list1=[]
        list2=[]
        
        tall1=height(root1)
        tall2=height(root2)
        if tall1!=tall2:
            return False
        
        for i in range(tall1):
            traversal(root1,i,list1)
            traversal(root2,i,list2)
            if list1!=list2[::-1]:
                return False
            list1=[]
            list2=[]
        return True
