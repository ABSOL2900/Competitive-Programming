class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        nonzeropointer=0
        zeropointer=0
        
        while zeropointer<len(nums):
            if nums[zeropointer]!=0:
                temp=nums[zeropointer]
                nums[zeropointer]=nums[nonzeropointer]
                nums[nonzeropointer]=temp
                nonzeropointer+=1
                
            zeropointer+=1
            
        print(nums)
            