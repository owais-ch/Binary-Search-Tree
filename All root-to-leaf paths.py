'''Given the roots of a tree. print out all of its root-to-leaf paths one per line.. '''
class Tree:
  def__init__(self,data):
    self.data=data
    self.left=None
    self.right=None
    
def root_to_leaf(root,arr):
    global list1
    
    if root==None:
        return True
    
    list1.append(root.data)
    
    if root.left==None and root.right==None:
        arr.append(list1.copy())
        list1.pop()
        return True
        
    if root.left:
        root_to_leaf(root.left,arr)
    if root.right:
        root_to_leaf(root.right,arr)
        
    return False
  

root = Tree(1)
root.left = Tree(2)
root.right = Tree(3)
root.left.left = Tree(4)
root.left.right = Tree(5)
root.left.right.right = Tree(15)
root.right.left = Tree(6)
root.right.right = Tree(7)
root.right.left.right = Tree(8)
 
node1 = root.left.right.data
node2 = root.right.right.data

arr=[]
list1=[]
root_to_leaf(root,arr)
print(arr)
    
