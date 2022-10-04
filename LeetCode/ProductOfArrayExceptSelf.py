class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefixproduct=[]
        postfixproduct=[]
        output=[]
        totalpre=1
        totalpost=1
        
        for num in nums:
            totalpre*=num
            prefixproduct.append(totalpre)
        for num in reversed(nums):
            totalpost*=num
            postfixproduct.append(totalpost)
            
        postfixproduct.reverse()

        output.append(1*postfixproduct[1])
        i=1
        while i < len(nums)-1:
            output.append(prefixproduct[i-1] * postfixproduct[i+1])
            i+=1
            
        output.append(1*prefixproduct[-2])
        

            
            
        return output