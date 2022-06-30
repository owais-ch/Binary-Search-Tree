'''Given a Binary Search Tree, find the sum of all leaf nodes. BST has the following property (duplicate nodes are possible):

The left subtree of a node contains only nodes with keys less than the node’s key.
The right subtree of a node contains only nodes with keys greater than or equal to the node’s key.
Input:
The first line of input contains a single integer T denoting the number of test cases. Then T test cases follow. Each test case consists of two lines. The first line of each test case consists of integer N, denoting the number of elements in the BST. The second line of each test case consists of N space-separated integers denoting the elements in the BST.

Output:
For each testcase, in a new line, print the sum of leaf nodes.'''

def sumOfLeafNodes(root):
    def traversal(root):
        nonlocal sum1
        
        if root==None:
            return None
        
        if root.left==None and root.right==None:
            sum1+=root.data
        if root.left:
            traversal(root.left)
        if root.right:
            traversal(root.right)
    
    sum1=0
    traversal(root)
    return sum1
