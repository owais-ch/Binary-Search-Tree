'''Given a binary tree of N nodes, where every node value is a number. Find the sum of all the numbers which are formed from root to leaf paths.

Example 1:

Input :      
           6                               
         /   \                          
        3     5                      
      /   \     \
     2    5      4             
        /  \                        
       7    4  

Output: 13997'''

def treePathSum(root):
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
            list1.append(root)
            if root.left==None and root.right==None:
                list2.append(root)
        else:
            traversal(root.left,level-1)
            traversal(root.right,level-1)
    if root.left==None and root.right==None:
        return root.data
    
    tall=height(root)
    list1=[]
    list2=[]
    for i in range(tall-1,-1,-1):
        traversal(root,i)
        
    length=len(list1)
    list4=[]
    for i in range(1,length):
        compare=list1[i-1]
        list3=[compare.data]
        if compare in list2:
            for j in range(i,length):
                if list1[j].left==compare or list1[j].right==compare:
                    compare=list1[j]
                    list3.append(compare.data)
                    
            list4.append(int(''.join(list(map(str,list3))[::-1])))
            list3=[]
            
    return sum(list4)
