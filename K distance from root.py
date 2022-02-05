'''Given a Binary Tree of size N and an integer K. Print all nodes that are at distance k from root (root is considered at distance 0 from itself).
Nodes should be printed from left to right. If k is more that height of tree, nothing should be printed.

For example, if below is given tree and k is 2. Output should be 4 5 6.

          1
       /     \
     2        3
   /         /   \
  4        5    6 
     \
      8'''

def KDistance(root,k):
    def height(root):
        if root==None:
            return 0
        left=height(root.left)
        right=height(root.right)
        
        return max(left,right)+1
        
    tall=height(root)
    list1=[]
    
    def level_traversal(root,level):
        if root==None:
            return None
        elif level==0:
            list1.append(root.data)
        else:
            level_traversal(root.left,level-1)
            level_traversal(root.right,level-1)
            
    for i in range(tall):
        level_traversal(root,i)
        if i==k:
            return list1
        list1=[]
        
    return []
