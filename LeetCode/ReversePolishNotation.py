class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        
        operators=["*","/","-","+"]
        stack=[]
        for token in tokens:
            
            if token not in operators:
                stack.append(int(token))
                
            else: 
                firstoperand=stack.pop()
                secondoperand=stack.pop()
                
               
                
                if token=="*" :
                    stack.append(firstoperand*secondoperand)
                    
                elif token=="/" :
                    stack.append(int(secondoperand/firstoperand))
                elif token=="-":
                    stack.append(secondoperand-firstoperand)
                else:
                    stack.append(firstoperand+secondoperand)
               
                
        return stack.pop()     
                
            
            
        