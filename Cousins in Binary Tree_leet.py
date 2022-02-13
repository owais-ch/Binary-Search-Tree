'''Given the root of a binary tree with unique values and the values of two different nodes of the tree x and y, return true if the nodes corresponding to the values x
and y in the tree are cousins, or false otherwise.

Two nodes of a binary tree are cousins if they have the same depth with different parents.

Note that in a binary tree, the root node is at the depth 0, and children of each depth k node are at the depth k + 1.

Example 1:

Input: root = [1,2,3,4], x = 4, y = 3
Output: false'''

class Solution:
    def __init__(self):
        self.list1=[]
    def isCousins(self, root, x: int, y: int) -> bool:
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
                if root.left:
                    if root.left.val==x:
                        self.list1.append([root.val,x])
                    if root.left.val==y:
                        self.list1.append([root.val,y])
                        
                if root.right:
                    if root.right.val==x:
                        self.list1.append([root.val,x])
                    if root.right.val==y:
                        self.list1.append([root.val,y])   
                    
            else:
                traversal(root.left,level-1)
                traversal(root.right,level-1)
                
                
                
        tall=height(root)
        
        for i in range(tall):
            traversal(root,i)
            if len(self.list1)==1:
                return False
            elif len(self.list1)==2:
                break
            
        
        if len(self.list1)==1:
            return False
        if self.list1[0][0]!=self.list1[1][0]:
            return True
        else:
            return False
