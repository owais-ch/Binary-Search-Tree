'''Given the root of a binary tree, the level of its root is 1, the level of its children is 2, and so on.

Return the smallest level x such that the sum of all the values of nodes at level x is maximal.

Example 1:

Input: root = [1,7,0,7,-8,null,null]
Output: 2
Explanation: 
Level 1 sum = 1.
Level 2 sum = 7 + 0 = 7.
Level 3 sum = 7 + -8 = -1.
So we return the level with the maximum sum which is level 2.'''

class Solution:
    def __init__(self):
        self.list1=[]
    def maxLevelSum(self, root) -> int:
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
        list2=[]
        count=0
        for i in range(tall):
            traversal(root,i)
            list2.append(sum(self.list1[count]))
            count+=1
            
        return list2.index(max(list2))+1
