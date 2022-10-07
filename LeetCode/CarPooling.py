class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        res=True
        sum=0
        journeys=sorted(trips,key=lambda d: d[1])
        prefixsum=[]

        for i in range(len(journeys)):

            for trip in prefixsum:
                if trip["dest"]<=journeys[i][1] and trip["finished"]==False:
                    
                    sum=sum-trip["ppl"]
                    trip["finished"]=True
            prefixsum.append({"ppl":journeys[i][0],"dest":journeys[i][2],"finished":False})
            sum=sum+journeys[i][0]

            if sum>capacity:
                return False

        
        return res
        