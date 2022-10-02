class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        stack=[]
        res=[]
        output=[-1]*len(nums1)
        
        for i in range(len(nums2)):
            
            while stack and nums2[i]>stack[-1]:
                res.append([stack.pop(),nums2[i]])
                
                
            if(nums2[i] in nums1):
                
                stack.append(nums2[i])
                
        for j in range(len(res)):
            index=nums1.index(res[j][0])
            output[index]=res[j][1]
                
            
        return output