'''Given the root of a binary tree, return the bottom-up level order traversal of its nodes' values. (i.e., from left to right, level by level from leaf to root).

Example 1:

Input: root = [3,9,20,null,null,15,7]
Output: [[15,7],[9,20],[3]]'''

class Solution:
    def __init__(self):
        self.list1=[]
    def levelOrderBottom(self, root):
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
                self.list1[count].append(root.val)
            else:
                traversal(root.left,level-1)
                traversal(root.right,level-1)
                
        tall=height(root)
        self.list1=[[] for i in range(tall)]
        count=0
        
        for i in range(tall):
            traversal(root,i)
            count+=1
            
        return self.list1[::-1]
