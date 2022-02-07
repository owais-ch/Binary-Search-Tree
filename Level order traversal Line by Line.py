'''Given a Binary Tree, your task is to find its level order traversal.
For the below tree the output will be 1 $ 2 3 $ 4 5 6 7 $ 8 $.

          1
       /     \
     2        3
   /    \     /   \
  4     5   6    7
    \
     8'''

def levelOrder(root):
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
            list1[count].append(root.data)
        else:
            traversal(root.left,level-1)
            traversal(root.right,level-1)
            
    tall=height(root)
    list1=[[] for i in range(tall)]
    count=0
    for i in range(tall):
        traversal(root,i)
        count+=1
    return list1
