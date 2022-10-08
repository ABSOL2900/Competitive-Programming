class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        
        lastindex={}
        for i in range(len(s)):
            lastindex[s[i]]=i
        
        
        size=0
        end=0
        res=[]
        for i in range(len(s)):
            size+=1
            if lastindex[s[i]]>end:
                end=lastindex[s[i]]
            if i==end:
                res.append(size)
                size=0

        return res
            