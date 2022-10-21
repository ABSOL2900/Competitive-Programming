class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        res=[]
        place=len(arr)-1
        
        top=-1
        
        while place!=0:
            top=self.getmax(arr,place+1)
            if top!=place:
                self.flip(arr,top)
                res.append(top+1)
                self.flip(arr,place)
                res.append(place+1)
            place-=1
        return res
        
        
        
        
    def getmax(self, arr: List[int], place:int):
        
        top=0
        ind=-1
        for i in range(0,place):
            if arr[i]>top:
                top=arr[i]
                ind=i
        
        
        return ind
    
    def flip(self, arr: List[int], to:int):
        left=0
        right=to
        
        while left<right:
            arr[left], arr[right]= arr[right], arr[left]
            left+=1
            right-=1