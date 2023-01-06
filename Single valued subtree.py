'''
Given a binary tree, count the number of Single Valued Subtrees. A Single Valued Subtree is one in which all the nodes have same value. 

Example 1

Input :
              5
             / \
            1   5
           / \   \
          5   5   5
Output : 4
Explanation : 
There are 4 subtrees with single values.
'''

class Solution:
    def singlevalued(self, root):
        def traversal(root):
            nonlocal count
            
            if root==None:
                return None
                
            if root.left:
                traversal(root.left)
                
            if root.right:
                traversal(root.right)
            
            if root.left and root.right:
                if root.left.data==root.right.data==root.data:
                    count+=1
                elif root.left.data==root.right.data and root.left.data!=root.data:
                    root.data=-9999999
                elif root.left.data!=root.data:
                    root.data=root.left.data
            elif root.left:
                if root.left.data==root.data:
                    count+=1
                else:
                    root.data=-999999999
            elif root.right:
                if root.right.data==root.data:
                    count+=1
                else:
                    root.data=-11111111
            elif root.left==None and root.right==None:
                count+=1
                
        count=0
        
        traversal(root)
        
        return count
