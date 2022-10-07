class Solution:
    def chalkReplacer(self, chalk: List[int], k: int) -> int:
        
        Sum=sum(chalk)
        num=int(k/Sum)
        k-=Sum*num
        replacer=-1
        
        loop=True
        while loop==True:
            
            for i in range(len(chalk)):
                
                if chalk[i]>k:
                    replacer=i
                    loop=False
                    break
                k-=chalk[i]
        return replacer
            
            
             