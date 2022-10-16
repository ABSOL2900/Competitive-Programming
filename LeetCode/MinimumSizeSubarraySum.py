class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        
        left=0
        right=0
        val=0
        res=0
        
        while right<len(nums):
            
            val+=nums[right]
            if val>=target:
                while val-nums[left]>=target and left<right:
                    val=val-nums[left]
                    left+=1
                res=min(right-left+1,res) if res!=0 else right-left+1
            
            right+=1
            
        return res