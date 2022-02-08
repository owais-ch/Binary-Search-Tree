'''Given the root of a binary tree, check whether it is a mirror of itself (i.e., symmetric around its center).

Example 1:

Input: root = [1,2,2,3,4,4,3]
Output: true'''

class Solution:
    def __init__(self):
        self.list1=[]
    def isSymmetric(self, root) -> bool:
        def height(root):
            if root==None:
                return 0
            
            left=height(root.left)
            right=height(root.right)
            
            return max(left,right)+1
        
        def traversal(root,level):
            if root==None:
                self.list1.append(None)
                return
                
            if level==0:
                self.list1.append(root.val)
            else:
                traversal(root.left,level-1)
                traversal(root.right,level-1)
                
                
        tall=height(root)
        
        for i in range(1,tall):
            traversal(root,i)
            if len(self.list1)%2!=0:
                return False
            else:
                if self.list1[:len(self.list1)//2]!=self.list1[len(self.list1)//2:][::-1]:
                    return False
            self.list1=[]    
        return True
