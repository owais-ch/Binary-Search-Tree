'''Given the root of a binary tree, return the sum of every tree node's tilt.

The tilt of a tree node is the absolute difference between the sum of all left subtree node values and all right subtree node values. If a node does not have a left child, then the sum of the left subtree node values is treated as 0. The rule is similar if the node does not have a right child.

Example 1:

Input: root = [1,2,3]
Output: 1
Explanation: 
Tilt of node 2 : |0-0| = 0 (no children)
Tilt of node 3 : |0-0| = 0 (no children)
Tilt of node 1 : |2-3| = 1 (left subtree is just left child, so sum is 2; right subtree is just right child, so sum is 3)
Sum of every tilt : 0 + 0 + 1 = 1'''

class Solution:
    def __init__(self):
        self.list1=[]
    def findTilt(self, root) -> int:
        def traversal(root):
            if root==None:
                return None
            if root.left:
                traversal(root.left)
            self.list1.append(root)    
            if root.right:
                traversal(root.right)
                
        def traversal2(root):
            nonlocal total_sum
            if root==None:
                return None
            
            traversal(root)
            
            length=len(self.list1)
            
            first=True
            
            x1=0
            x2=0
            
            for i in range(length):
                if self.list1[i]!=root and first==True:
                    x1+=self.list1[i].val
                elif self.list1[i]==root:
                    first=False
                elif self.list1[i]!=root and first==False:
                    x2+=self.list1[i].val
            self.list1=[]        
            root.val=abs(x1-x2)
            total_sum+=root.val
            
            if root.left:
                traversal2(root.left)
                
            if root.right:
                traversal2(root.right)
                
        total_sum=0
        traversal2(root)
        
        return total_sum
