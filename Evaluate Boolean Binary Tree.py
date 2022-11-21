'''You are given the root of a full binary tree with the following properties:

Leaf nodes have either the value 0 or 1, where 0 represents False and 1 represents True.
Non-leaf nodes have either the value 2 or 3, where 2 represents the boolean OR and 3 represents the boolean AND.
The evaluation of a node is as follows:

If the node is a leaf node, the evaluation is the value of the node, i.e. True or False.
Otherwise, evaluate the node's two children and apply the boolean operation of its value with the children's evaluations.
Return the boolean result of evaluating the root node.

A full binary tree is a binary tree where each node has either 0 or 2 children.

A leaf node is a node that has zero children.

 

Example 1:


Input: root = [2,1,3,null,null,0,1]
Output: true
Explanation: The above diagram illustrates the evaluation process.
The AND node evaluates to False AND True = False.
The OR node evaluates to True OR False = True.
The root node evaluates to True, so we return true.
'''

class Solution:
    def evaluateTree(self, root: Optional[TreeNode]) -> bool:
        if root==None:
            return None
        if root.left==None and root.right==None:
            return root.val

        if root.left:
            self.evaluateTree(root.left)

        if root.right:
            self.evaluateTree(root.right)

        if root.val==2:
            root.val=root.left.val or root.right.val
        elif root.val==3:
            root.val=root.left.val and root.right.val

        return root.val
