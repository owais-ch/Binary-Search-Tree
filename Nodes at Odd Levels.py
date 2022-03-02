'''Given a binary tree of size N, find all the nodes at odd levels.Root is considered at level 1.

Example 1:

Input: 
          1
       /     \
      2       3
    /   \       \
   4     5       6
        /  \     /
       7    8   9

Output  1 4 5 6'''

class Solution:
    def nodesAtOddLevels(self,root):
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
        count=1
        list1=[]
        for i in range(tall):
            if count%2!=1:
                traversal(root,i)
                
        return list1
