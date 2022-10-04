class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        result=0
        prefixsum={0:1}
        currsum=0
        
        for num in nums:
            currsum+=num
            diff=currsum-k
            
            result+=prefixsum.get(diff,0)
            prefixsum[currsum]=1+prefixsum.get(currsum,0)
            
        return result
                 
                
                
            