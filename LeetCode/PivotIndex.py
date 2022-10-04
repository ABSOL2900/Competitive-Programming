class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        leftsum=0
        totalsum=0
        
        pivot=-1
        for num in nums:
            totalsum+=num
        
        for i in range(len(nums)):
            if i!=0:
                leftsum+=nums[i-1]
                
            rightsum=totalsum-nums[i]-leftsum
            if rightsum==leftsum:
                print(nums[i])
                pivot=i
                break
                
        return pivot
                
            