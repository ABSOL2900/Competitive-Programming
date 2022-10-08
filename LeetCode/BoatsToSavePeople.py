class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        
        people.sort(key=lambda x : -x)
        maxpointer=0
        minpointer=len(people)-1
        boats=0
        
        while maxpointer<=minpointer :
            
            if people[maxpointer] + people[minpointer]<=limit  :
                minpointer-=1
            maxpointer+=1
            boats+=1
            
        return boats