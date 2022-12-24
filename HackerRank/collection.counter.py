# Enter your code here. Read input from STDIN. Print output to STDOUT
    
shoenumber= int(input())
shoesizes =list(map(int, input().split(" ")))
customernumber=int(input())
customerneed=[]
moneyearned=0
for _ in range(customernumber):
    customerneedinput =list(map(int, input().split(" ")))
    customerneed.append(customerneedinput)
for cneed in customerneed:
    if cneed[0] in shoesizes:
        moneyearned+=cneed[1]
        shoesizes.remove(cneed[0])
        
print(moneyearned)

