class Solution:
    def reverseParentheses(self, s: str) -> str:
        
        stack1=[]
        stack2=[]

        for i in range(len(s)):
            if s[i]!=')':
                stack1.append(s[i])
            else :
                popped=stack1.pop()
                while popped!='(':
                    
                    stack2.append(popped)
                    popped=stack1.pop()

                    
            
            stack1=stack1+stack2
            stack2=[]
        
        return "".join(stack1)
            
        