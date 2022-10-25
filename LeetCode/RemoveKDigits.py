class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        
        stack=[num[0]]
        
        for i in range(1,len(num)):
            
            while stack and  stack[-1]>num[i] and k>0:
                stack.pop()
                k-=1
            
            stack.append(num[i])
        
        
        stack=stack[:len(stack)-k]
            
        
        
            
        return str(int("".join(stack))) if "".join(stack) else "0"
                
            
            