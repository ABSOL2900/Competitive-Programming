class Solution:
    def isValid(self, s: str) -> bool:
        opening =['(','{','[']
        closing=[')','}',']']
        both=[['{','}'],['(',')'],['[',']']]
        slist=[]
        
        for i in range(len(s)):
            if s[i] in opening and len(slist)==0:
                slist.append(s[i])
            elif s[i] in opening and len(slist)!=0 :
                if slist[-1] in opening: 
                    slist.append(s[i])
                else:
                    return False
            elif s[i] in closing and len(slist)==0:
                return False
            elif s[i] in closing and len(slist)!=0 :
                if  slist[-1] in opening :
                    found=False
                    for j in range(len(both)):
                        if(s[i]==both[j][1] and slist[-1]==both[j][0]) :
                            slist.pop()
                            found=True
                            break
                    if found==False:
                        return False
                        
                elif slist[-1] in closing:
                    return False
        
        return len(slist)==0
                