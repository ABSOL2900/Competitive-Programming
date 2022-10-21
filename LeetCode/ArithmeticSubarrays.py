class Solution:
    def checkArithmeticSubarrays(self, nums: List[int], l: List[int], r: List[int]) -> List[bool]:
        res=[]
        for i in range(len(l)):
            start=l[i]
            end=r[i]
            arr=[]
            
            for j in range(start,end+1):
                
                arr.append(nums[j])
            
            arr.sort()
            if len(arr)==2:
                res.append(True)
            else:
                val=True
                diff=arr[1]-arr[0]
                for k in range(2,len(arr)):
                    if arr[k]-arr[k-1]!=diff:
                        val=False
                        break
                res.append(val)
        return res
                        
                
            