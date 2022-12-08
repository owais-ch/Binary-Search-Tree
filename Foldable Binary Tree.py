'''Given a binary tree, check if the tree can be folded or not
. A tree can be folded if left and right subtrees of the tree are structure wise mirror image of each other. An empty tree is considered as foldable.
'''

def IsFoldable(root):
    def traversal(root1,root2):
        if root1==None and root2==None:
            return True
        elif root1!=None and root2!=None:
            return traversal(root1.left,root2.right) and traversal(root1.right,root2.left)
        else:
            return False
            
    return traversal(root,root)
