'''Given an array arr[] of N nodes representing preorder traversal of BST. The task is to print its postorder traversal.
In Pre-Order traversal, the root node is visited before the left child and right child nodes.
Post-order traversal is one of the multiple methods to traverse a tree.

Example 1:

Input:
N = 5
arr[]  = {40,30,35,80,100}
Output: 35 30 100 80 40
Explanation: PreOrder: 40 30 35 80 100
InOrder: 30 35 40 80 100
Therefore, the BST will be:
              40
           /      \
         30       80
           \        \   
           35      100
Hence, the postOrder traversal will
be: 35 30 100 80 40'''


def post_order(arr, size):
    
    def buildBST(list1,start,end):
        if start>end:
            return None
            
        
        root=Node(list1[start])

        i=start
        while i<=end:
            if list1[i]>root.data:
                break
            i+=1

        
        root.left=buildBST(list1,start+1,i-1)
        root.right=buildBST(list1,i,end)
        
        return root
        
        
    return buildBST(arr,0,len(arr)-1) 
