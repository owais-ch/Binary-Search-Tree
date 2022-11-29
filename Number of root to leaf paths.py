'''Given a binary tree, you need to find the number of all root to leaf paths along with their path lengths.

Example 1:

Input:
      3
    /   \
   2     4
Output:
2 2 $

Explanation :
There are 2 roots to leaf paths
of length 2(3 -> 2 and 3 -> 4)
'''


def pathCounts(root):
    def traversal(root):
        nonlocal count
        
        if root==None:
            return None
            
        count+=1
        
        if root.left==None and root.right==None:
            if count not in dict1:
                dict1[count]=1
            else:
                dict1[count]+=1
                
        if traversal(root.left) or traversal(root.right):
            return True
            
        count-=1
        
        return False
        
    count=0
    
    dict1=dict()
    
    traversal(root)
    
    string=''
    arrx=sorted(list(dict1.items()),key=lambda x:[0])
    
    for i in arrx:
        string+=str(i[0])+' '+str(i[1])+' $'
    
    print(string)
