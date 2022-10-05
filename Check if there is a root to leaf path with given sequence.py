'''Given a binary tree and an array, the task is to find if the given array sequence is present as a root to leaf path in given tree.

Examples :

Input : arr[] = {5, 2, 4, 8} for above tree
Output: "Path Exist"

Input :  arr[] = {5, 3, 4, 9} for above tree
Output: "Path does not Exist"'''

def path_exist(root,arr,list1):
    global value
    if root==None:
        return False
    
    arr.append(root.data)
    
    if root.left==None and root.right==None:
        print(arr)
        if arr==list1:
            value='exist'
            return 'Exist'
        
    if path_exist(root.left,arr,list1) or path_exist(root.right,arr,list1):
        return True
    
    arr.pop()
    
    return False


list1 = [5, 3,5]

n = len(list1)
value='dont exist'
root = Tree(5)
root.left = Tree(3)
root.right = Tree(8)
root.left.left = Tree(2)
root.left.right = Tree(4)
root.left.left.left = Tree(1)
root.right.left = Tree(6)
root.right.left.right = Tree(7)

arr=[]

path_exist(root,arr,list1)
value   
