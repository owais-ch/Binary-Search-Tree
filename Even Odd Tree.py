'''A binary tree is named Even-Odd if it meets the following conditions:

The root of the binary tree is at level index 0, its children are at level index 1, their children are at level index 2, etc.
For every even-indexed level, all nodes at the level have odd integer values in strictly increasing order (from left to right).
For every odd-indexed level, all nodes at the level have even integer values in strictly decreasing order (from left to right).
Given the root of a binary tree, return true if the binary tree is Even-Odd, otherwise return false.

Example 1:

Input: root = [1,10,4,3,null,7,9,12,8,6,null,null,2]
Output: true'''

from collections import deque

class Solution:
    def __init__(self):
        self.list1=[]
    def isEvenOddTree(self, root) -> bool:
        def traversal(root):
            if not root:
                return []
            level=0
            q = deque([root])
            while q:
                levelLen = len(q)
                levelNodes = []
                for i in range(levelLen):
                    curNode = q.popleft()
                    self.list1.append(curNode.val)
                    if curNode.left:
                        q.append(curNode.left)
                    if curNode.right:
                        q.append(curNode.right)
                if len(self.list1)!=len(set(self.list1)):
                    print(11111111)
                    return False
                
                if level%2==0:
                    
                    if self.list1!=sorted(self.list1):
                        return False
                    for i in self.list1:
                        if i%2==0:
                            return False
                else:
                    if self.list1!=sorted(self.list1,reverse=True):
                        return False
                    for i in self.list1:
                        if i%2!=0:
                            return False
                
                level+=1    
                self.list1=[]
                   
            return True    
        
        
        return traversal(root)
