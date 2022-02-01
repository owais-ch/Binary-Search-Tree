'''You are given the root of a binary search tree(BST), where exactly two nodes were swapped by mistake. Fix (or correct) the BST by swapping them back. Do not change the structure of the tree.
Note: It is guaranteed that the given input will form BST, except for 2 nodes that will be wrong. All changes must be reflected in the original linked list.
 
Example 1:
Input:
       10
     /    \
    5      8
   / \
  2   20
Output: 1'''


class Solution:
    def __init__(self):
        self.list1=[]
        self.list2=[]
    def correctBST(self, root):
        def traversal(root):
            if root.left:
                traversal(root.left)
                
            self.list1.append(root.data)
            self.list2.append(root)
                
            if root.right:
                traversal(root.right)
                
        traversal(root)
        
        list2=sorted(self.list1)
        
        list3=[]
        list4=[]
        
        length=len(self.list1)
        
        for i in range(length):
            if list2[i]!=self.list1[i]:
                list3.append(self.list1[i])
                list4.append(self.list2[i])
                if len(list3)==2:
                    break
            
                    
        list4[0].data,list4[1].data=list4[1].data,list4[0].data
        
        return root
