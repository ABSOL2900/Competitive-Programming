class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        
        res=0
        
        left=0
        right=len(nums)-1
        nums.sort()
        
        while left<right:
            res=max(res,nums[right]+nums[left])
            left+=1
            right-=1
        return res