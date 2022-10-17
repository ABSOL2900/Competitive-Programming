class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        arr=[[] for i in range(len(nums)+1)]
        
        nums.sort()
        count=0
        val=nums[0]
        
        for i in nums:
            if val==i:
                count+=1
            else:
                arr[count].append(val)
                val=i
                count=1
        arr[count].append(val)
        
        res=[]
        
        for j in range(len(nums),0,-1):
            for n in arr[j]:
                res.append(n)
                if len(res)==k:
                    return res
                    
        