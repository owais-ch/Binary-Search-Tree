'''You are given the root of a binary tree A.
You have to find out the number of parent - child relationship whose values are consecutive numbers.'''


class Solution:
    def consecutiveNodes(self, root):
        def traversal(root):
            nonlocal count
            if root==None:
                return None

            if root.left:
                if abs(root.val-root.left.val)==1:
                    count+=1
            if root.right:
                if abs(root.val-root.right.val)==1:
                    count+=1

            if root.left:
                traversal(root.left)

            if root.right:
                traversal(root.right)

        count=0

        traversal(root)

        return count

