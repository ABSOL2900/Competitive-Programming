class Solution:
    def findMaxConsecutiveOnes(self, nums) :
        
        res=0

        temp=0        
        
        for i in nums:
            
            if i==1:
                temp+=1
            else:
                res=max(res,temp)
                temp=0
            

                
            
            
            
        return max(res,temp)

