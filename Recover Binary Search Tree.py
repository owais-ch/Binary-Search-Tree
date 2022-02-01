'''You are given the root of a binary search tree (BST), where the values of exactly two nodes of the tree were swapped by mistake. Recover the tree without changing its structure.

Example 1:

Input: root = [1,3,null,null,2]
Output: [3,1,null,null,2]
Explanation: 3 cannot be a left child of 1 because 3 > 1. Swapping 1 and 3 makes the BST valid.'''

class Solution:
    def __init__(self):
        self.list1=[]
        self.list2=[]
    def recoverTree(self, root):
        def traversal(root):
            if root.left:
                traversal(root.left)
                
            self.list1.append(root.val)
            self.list2.append(root)
            
            if root.right:
                traversal(root.right)
                
        traversal(root)
        
        list3=sorted(self.list1)
        
        list4=[]
        
        length=len(self.list1)
        
        for i in range(length):
            if list3[i]!=self.list1[i]:
                list4.append(self.list2[i])
                if len(list4)==2:
                    break
                    
        list4[0].val,list4[1].val=list4[1].val,list4[0].val
        
        return root
