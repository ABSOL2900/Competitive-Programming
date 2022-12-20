# Enter your code here. Read input from STDIN. Print output to STDOUT
def wordwrap():
    num=int(input())
    wordarray={}
    for i in range(num):
        word=input()
        if word in wordarray:
            wordarray[word]=wordarray[word]+1
        else:
            wordarray[word]=1
    output=[]
    print(len(wordarray))
    for v in wordarray.values():
        output.append(v)
    print(*output)
        
wordwrap()
            
    