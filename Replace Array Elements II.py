'''

Given an array of distinct integers, replace every element with the least greater element on its right or with -1 if there are no greater elements.

Input : [10, 100, 93, 32, 35, 65, 80, 90, 94, 6]
Output: [32, -1, 94, 35, 65, 80, 90, 94, -1, -1]

'''

class Solution:
    def replace(self, nums) -> None:
        if nums==[]:
        	return nums

        stack=[nums[-1]]
		nums[-1]=-1
        length=len(nums)

        for i in range(-2,-length-1,-1):
            if nums[i]>stack[-1]:
            	stack.append(nums[i])
                nums[i]=-1
            else:
            	stack.append(nums[i])
                for j in range(len(stack)):
                    if stack[j]>nums[i]:
                        nums[i]=stack[j]
                        break
            
            

            stack.sort()

        return nums
