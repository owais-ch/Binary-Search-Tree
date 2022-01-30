'''Given a Singly Linked List which has data members sorted in ascending order. Construct a Balanced Binary Search Tree which has same data members as the given Linked List.
Note: There might be nodes with same value.

Example 1:

Input:
Linked List: 1->2->3->4->5->6->7
Output:
4 2 1 3 6 5 7'''


class Solution:
    def sortedArrayToBST(self, nums):
        def buildBST(nums):
            if not nums:
                return None
            
            mid=len(nums)//2
            
            root=TreeNode(nums[mid])
            
            root.left=buildBST(nums[:mid])
            root.right=buildBST(nums[mid+1:])
            
            return root
        
        return buildBST(nums)
