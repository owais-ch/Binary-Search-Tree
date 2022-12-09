'''
Given a binary tree root, a node X in the tree is named good if in the path from root to X there are no nodes with a value greater than X.

Return the number of good nodes in the binary tree.

Example 1:

Input: root = [3,1,4,3,null,1,5]
Output: 4
Explanation: Nodes in blue are good.
Root Node (3) is always a good node.
Node 4 -> (3,4) is the maximum value in the path starting from the root.
Node 5 -> (3,4,5) is the maximum value in the path
Node 3 -> (3,1,3) is the maximum value in the path.
'''

class Solution:
    def __init__(self):
        self.list1=[]
        self.count=0
    def goodNodes(self, root: TreeNode) -> int:
        def root_node(root):
            nonlocal maximum,count

            if root==None:
                return None

            if root.val>=maximum:
                maximum=root.val
                stack.append(root.val)
                count+=1

            if root_node(root.left) or root_node(root.right):
                return True

            if root.val==maximum:
                stack.pop()
                if stack!=[]:
                    maximum=stack[-1]
                else:
                    maximum=-9999

            return False

        count=0
        maximum=-9999
        stack=[]

        root_node(root)

        return count
