'''Given a Binary Search Tree (BST) and a range l-h(inclusive), count the number of nodes in the BST that lie in the given range.

The values smaller than root go to the left side
The values greater and equal to the root go to the right side
Example 1:

Input:
      10
     /  \
    5    50
   /    /  \
  1    40  100
l = 5, h = 45
Output: 3
Explanation: 5 10 40 are the node in the
range'''

def getCount(root,low,high):
    def traversal(root):
        if root==None:
            return None
            
        list1.append(root.data)
        
        if root.left:
            traversal(root.left)
            
        if root.right:
            traversal(root.right)
            
    list1=[]
    
    traversal(root)
    
    count=0
    
    for i in list1:
        if i>=low and i<=high:
            count+=1
            
    return count
