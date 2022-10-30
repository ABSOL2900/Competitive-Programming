class Solution:
    def minIncrementForUnique(self, nums) -> int:

        nums.sort()
        prev=nums[0]
        inc=0
        
        
        for i in range(1,len(nums)):
            if nums[i]<=prev:
                inc+=(prev+1)-nums[i]
                nums[i]=prev+1
                
            prev=nums[i]
        
        print(inc)

soln=Solution()

soln.minIncrementForUnique([3,2,1,2,1,7])
                
                    
        