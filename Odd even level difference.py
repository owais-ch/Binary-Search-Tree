'''Given a Binary Tree. Find the difference between the sum of node values at even levels and the sum of node values at the odd levels.

Example 1:

Input:
            1
          /   \
         2     3

Output: -4

Explanation:
sum at odd levels - sum at even levels
= (1)-(2+3) = 1-5 = -4'''

from collections import deque

class Solution:
    def getLevelDiff(self, root):
        def traversal(root):
            nonlocal sum1,sum2
            q=deque([])
            q.append(root)
            level=0
            while len(q)>0:
                count=len(q)
                
                while count>0:
                    temp=q.popleft()
                    
                    if level%2==0:
                        sum1+=temp.data
                    else:
                        sum2+=temp.data
                    if temp.left:    
                        q.append(temp.left)
                    if temp.right:
                        q.append(temp.right)
                    
                    count-=1
                    
                level+=1    
        sum1=0
        sum2=0
        traversal(root)
        return sum1-sum2
