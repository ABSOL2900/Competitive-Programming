# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import Counter
def captain():
    
    k=int(input())
    rooms=list(map(int, input().split(" ")))
    counted=Counter(rooms)
    output=-1
    # print("counter",counted)
    for i in counted:
        if counted[i]==1:
            output=i
            
    
        
    print(output)
    
captain()
        