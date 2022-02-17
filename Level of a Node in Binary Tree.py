'''Given a Binary Tree and a target key you need to find the level of target key in the given Binary Tree.

Note: The level of the root node is 1.

           3
         /   \
        2     5
      /   \
     1     4
Key: 4
Level: 3  '''

class Solution:
    def getLevel(self, root,target):
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
        for i in range(tall):
            traversal(root,i)
            
            if target in list1:
                return i+1
            list1=[]
                
        return 0
