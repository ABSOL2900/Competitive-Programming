class Solution:
    def sortSentence(self, s: str) -> str:
        
        arr=s.split(" ")
        print(arr)
        arr2=["" for  i in arr]
        
        for i in arr:
            arr2[int(i[len(i)-1])-1]=i[:len(i)-1]
        return " ".join(arr2)
            