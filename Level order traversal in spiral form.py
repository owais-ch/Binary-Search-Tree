'''Complete the function to find spiral order traversal of a tree. 
Input:
           10
         /     \
        20     30
      /    \
    40     60
Output: 10 20 30 60 40 '''

def findSpiral(root):
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
            list1.append(root.data)
        else:
            traversal(root.left,level-1)
            traversal(root.right,level-1)
            
    list1=[]
    tall=height(root)
    list2=[]
    for i in range(tall):
        traversal(root,i)
        if i%2==0:
            list2.extend(list1[::-1])
        else:
            list2.extend(list1)
            
        list1=[]
        
    return list2
