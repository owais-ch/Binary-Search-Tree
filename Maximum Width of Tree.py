'''Given a Binary Tree, find the maximum width of it. Maximum width is defined as the maximum number of nodes in any level.
For example, maximum width of following tree is 4 as there are 4 nodes at 3rd level.

          1
       /     \
     2        3
   /    \    /    \
  4    5   6    7
    \
      8

Example 1:

Input:
       1
     /    \
    2      3
Output: 2'''

class Solution:
    def getMaxWidth(self,root):
        def height(root):
            if root==None:
                return 0
                
            left=height(root.left)
            right=height(root.right)
            
            return max(left,right)+1
            
        def traversal(root,level):
            if root==None:
                return None
                
            if level==0:
                list1.append(root.data)
            else:
                traversal(root.left,level-1)
                traversal(root.right,level-1)
                
        tall=height(root)
        
        list1=[]
        maximum=0
        
        for i in range(tall):
            traversal(root,i)
            maximum=max(maximum,len(list1))
            list1=[]
            
        return maximum
