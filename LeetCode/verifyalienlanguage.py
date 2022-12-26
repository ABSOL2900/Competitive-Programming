class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
            output=True
            leftp=0
            rightp=1
            while leftp<rightp and rightp<len(words):
                # print(words[leftp],words[rightp],output)
                sizeleft=len(words[leftp])
                sizeright=len(words[rightp])
                shorterword=sizeleft if sizeleft<sizeright else sizeright
                compared=0
                for i in range(shorterword):
                    leftchar=words[leftp][i]
                    rightchar=words[rightp][i]
                    posleft=order.find(leftchar)
                    posright=order.find(rightchar)
                    # print(posleft,posright)
                    if posleft>posright:
                        # print(posleft,posright)
                        output=False
                        break
                    elif posleft<posright:
                        break
                    elif posleft==posright:
                        compared+=1
                        
                if compared==shorterword and sizeright==shorterword and words[leftp]!=words[rightp]:
                    output=False
                    break
                # print(words[leftp],words[rightp],output)
                leftp+=1
                rightp+=1

                
            return output