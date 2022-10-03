class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        
        dictlists=[]
        stack=[]
        for i in range(len(position)):
            dictlists.append({'pos':position[i],'speed':speed[i]})
            
        dictlist=sorted(dictlists, key=lambda c: c['pos'],reverse=True)
        
        for car in dictlist:
            if stack:
                velocityofTop=(target-stack[-1]['pos'])/stack[-1]['speed']
                velocityofCar=(target-car['pos'])/car['speed']
                if  velocityofCar>velocityofTop:
                    stack.append(car)
            else:
                stack.append(car)
            
        return len(stack)