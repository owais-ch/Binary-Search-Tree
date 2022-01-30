'''Given the head of a singly linked list where elements are sorted in ascending order, convert it to a height balanced BST.

For this problem, a height-balanced binary tree is defined as a binary tree in which the depth of the two subtrees of every node never differ by more than 1.

Example 1:

Input: head = [-10,-3,0,5,9]
Output: [0,-3,9,-10,null,5]
Explanation: One possible answer is [0,-3,9,-10,null,5], which represents the shown height balanced BST.'''

class Solution:
    def sortedListToBST(self, head):
        n=head
        
        list1=[]
        
        while n!=None:
            list1.append(n.val)
            n=n.next
            
        def buildBST(nums):
            if not nums:
                return None
            
            mid=len(nums)//2
            
            root=TreeNode(nums[mid])
            
            root.left=buildBST(nums[:mid])
            root.right=buildBST(nums[mid+1:])
            
            return root
        
        return buildBST(list1)
