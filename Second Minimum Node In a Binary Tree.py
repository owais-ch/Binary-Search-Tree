'''Given a non-empty special binary tree consisting of nodes with the non-negative value, where each node in this tree has exactly two or zero sub-node. 
If the node has two sub-nodes, then this node's value is the smaller value among its two sub-nodes. More formally, the property root.val = min(root.left.val, root.right.val) always holds.

Given such a binary tree, you need to output the second minimum value in the set made of all the nodes' value in the whole tree.

If no such second minimum value exists, output -1 instead.

Example 1:

Input: root = [2,2,5,null,null,5,7]
Output: 5
Explanation: The smallest value is 2, the second smallest value is 5.'''

class Solution:
    def __init__(self):
        self.list1=[]
    def findSecondMinimumValue(self, root) -> int:
        def traversal(root):
            if root==None:
                return 
            
            if root.left:
                traversal(root.left)
                
            self.list1.append(root.val)
            
            if root.right:
                traversal(root.right)
                
        traversal(root)
        
        self.list1=list(set(self.list1))
        self.list1.sort()
        length=len(self.list1)
        
        if length<2:
            return -1
        else:
            return self.list1[1]
