class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        substr=""
        left=0
        right=0
        res=0
        while right<len(s):
            
            if s[right] in substr:
                left+=1
                i=substr.index(s[right])
                substr=substr[i+1:]
                
                
            
            
            substr+=s[right]
            res=max(res,len(substr))
            right+=1
            
        return res