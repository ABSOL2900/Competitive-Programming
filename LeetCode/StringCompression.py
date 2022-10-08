class Solution:
    def compress(self, chars: List[str]) -> int:
        
        chars.append("End")
        current=chars[0]
        times=0
        
        while current!="End":
            if current==chars[0]:
                chars.pop(0)
                times+=1
            else:
                chars.append(current)
                if times>1:
                    strvalue=str(times)
                    for j in range(len(strvalue)):
                        chars.append(strvalue[j])
                current=chars[0]
                times=0
        
        chars.pop(0)
        return len(chars)
                