'''Given the root of a binary tree and an integer targetSum, return all root-to-leaf paths where the sum of the node values in the path equals targetSum. 
Each path should be returned as a list of the node values, not node references.

A root-to-leaf path is a path starting from the root and ending at any leaf node. A leaf is a node with no children.
Example 1:
Input: root = [5,4,8,11,null,13,4,7,2,null,null,5,1], targetSum = 22
Output: [[5,4,11,2],[5,8,4,5]]
Explanation: There are two paths whose sum equals targetSum:
5 + 4 + 11 + 2 = 22
5 + 8 + 4 + 5 = 22'''

class Solution:
    def __init__(self):
        self.list1=[]
        self.list2=[]
    def pathSum(self, root, targetSum: int) -> List[List[int]]:
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
                self.list1.append(root)
            else:
                traversal(root.left,level-1)
                traversal(root.right,level-1)
                
        def traversal2(root,level):
            if root==None:
                return None
            
            if level==0:
                if root.left==None and root.right==None:
                    self.list2.append(root)
                    
            else:
                traversal2(root.left,level-1)
                traversal2(root.right,level-1)
        if root==None:
            return []
        elif root.left==None and root.right==None and root.val==targetSum:
            return [[root.val]]
        tall=height(root)
        
        for i in range(tall-1,-1,-1):
            traversal(root,i)
            traversal2(root,i)
        list5=[]    
        for i in range(1,len(self.list1)):
            total=0
            list4=[]
            
            if self.list1[i-1] in self.list2:
                compare=self.list1[i-1]
                total+=compare.val
                list4.append(compare.val)
                for j in range(i,len(self.list1)):
                    if self.list1[j].left==compare or self.list1[j].right==compare:
                        compare=self.list1[j]
                        list4.append(compare.val)
                        total+=compare.val
                        
            if total==targetSum and list4!=[]:
                list5.append(list4[::-1])
                
        return list5
