'''Implement the BSTIterator class that represents an iterator over the in-order traversal of a binary search tree (BST):

BSTIterator(TreeNode root) Initializes an object of the BSTIterator class. The root of the BST is given as part of the constructor.
The pointer should be initialized to a non-existent number smaller than any element in the BST.
boolean hasNext() Returns true if there exists a number in the traversal to the right of the pointer, otherwise returns false.
int next() Moves the pointer to the right, then returns the number at the pointer.
Notice that by initializing the pointer to a non-existent smallest number, the first call to next() will return the smallest element in the BST.

You may assume that next() calls will always be valid. That is, there will be at least a next number in the in-order traversal when next() is called.

 

Example 1:


Input
["BSTIterator", "next", "next", "hasNext", "next", "hasNext", "next", "hasNext", "next", "hasNext"]
[[[7, 3, 15, null, null, 9, 20]], [], [], [], [], [], [], [], [], []]
Output
[null, 3, 7, true, 9, true, 15, true, 20, false]'''

class BSTIterator:

    def __init__(self, root: Optional[TreeNode]):
        self.root=root
        self.count=0
        self.count2=0
        self.list1=[]
    def next(self) -> int:
        def traversal(root):
            if root.left:
                traversal(root.left)
                
            self.list1.append(root.val)
            
            if root.right:
                traversal(root.right)
        if self.count2==0 and self.count==0:        
            traversal(self.root)
        
        if self.count<len(self.list1):
            self.count+=1
            return self.list1[self.count-1]
        
    def hasNext(self) -> bool:
        def traversal(root):
            if root.left:
                traversal(root.left)
                
            self.list1.append(root.val)
            
            if root.right:
                traversal(root.right)
        if self.count==0 and self.count2==0:
            self.count2+=1
            traversal(self.root)
        if self.count<len(self.list1):
            return True
        return False
