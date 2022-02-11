'''Given a Binary tree. Find the level in binary tree which has the maximum number of nodes.

Example 1:

Input:
      2
    /    \ 
   1      3
 /   \     \
4    6      8
     / 
    5
Output: 2
Explanation: The level 2 with nodes 4, 6 and 8 is the level with maximum number of nodes. '''

def maxNodeLevel(root):
    def height(root):
        if root==None:
           return 0
           
        left=height(root.left)
        right=height(root.right)
        
        return max(left,right)+1
        
    def traversal(root,level):
        nonlocal count
        if root==None:
            return None
            
        if level==0:
            list1[count].append(root)
        else:
            traversal(root.left,level-1)
            traversal(root.right,level-1)
            
    count=0
    tall=height(root)
    list1=[[] for i in range(tall)]
    maximum=0
    level=0
    for i in range(tall):
        traversal(root,i)
        if len(list1[count])>maximum:
            maximum=len(list1[count])
            level=i
        count+=1
            
    return level
