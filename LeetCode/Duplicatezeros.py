class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        index=0
        while index<len(arr):
            if arr[index]==0:
                self.shiftarr(arr,index)
                index+=2
                continue
            index+=1



    def shiftarr(self,arr,index):
        zero=False
        nxt=arr[index]
        for i in range(index,len(arr)):
            if zero==False:
                arr[i]=0
                zero=True
            else:
                temp=arr[i]
                arr[i]=nxt
                nxt=temp