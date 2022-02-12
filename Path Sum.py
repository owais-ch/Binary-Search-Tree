'''Given the root of a binary tree and an integer targetSum, return true if the tree has a root-to-leaf path such that adding up all the values along the path equals targetSum.

A leaf is a node with no children.

Example 1:

Input: root = [5,4,8,11,null,13,4,7,2,null,null,null,1], targetSum = 22
Output: true
Explanation: The root-to-leaf path with the target sum is shown.'''

class Solution:
    def __init__(self):
        self.list1=[]
        self.list2=[]
    def hasPathSum(self, root, targetSum) -> bool:
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
                if root.left==None and root.right==None:
                    self.list1.append(root)
            else:
                traversal(root.left,level-1)
                traversal(root.right,level-1)
                
        def traversal2(root,level):
            if root==None:
                return None
            
            if level==0:
                self.list2.append(root)
            else:
                traversal2(root.left,level-1)
                traversal2(root.right,level-1)
        if root==None:
            return False
        elif root.left==None and root.right==None:
            if root.val==targetSum:
                return True
        
        tall=height(root)
        
        for i in range(tall-1,-1,-1):
            traversal(root,i)
            
        for i in range(tall-1,-1,-1):
            traversal2(root,i)
            
        for i in range(1,len(self.list2)):
            if self.list2[i-1] in self.list1:
                compare=self.list2[i-1]
                total=compare.val
                for j in range(i,len(self.list2)):
                    if self.list2[j].left==compare or self.list2[j].right==compare:
                        compare=self.list2[j]
                        total+=compare.val
                        
                if total==targetSum:
                    #print(total)
                    return True
                
        return False
