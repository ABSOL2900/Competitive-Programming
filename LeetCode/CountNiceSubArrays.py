class Solution:
    def numberOfSubarrays(self, nums, k):
        res=0
        odd=0
        count={0:0}
        
        
        for i in range(len(nums)):
            oddbool=False
            if(nums[i]%2!=0):
                odd+=1
                oddbool=True
            if odd==k:
                res+=1
                
            if odd>=k:
                for x, y in enumerate(count):
                    if(odd-k==y):
                        res+=1
     
            if oddbool==True:
                count[odd]=odd
            else:
                count[odd]=count[odd]+1
           
        print(count)
        print(res)

soln=Solution()
soln.numberOfSubarrays([2,2,2,1,2,2,1,2,2,2],2)
        
        
                
            