if __name__ == '__main__':
    N = int(input())
    commands=[]
    output=[]
    for _ in range(N):
        command=input()
        command=command.split(" ")
        commands.append(command)
    
    for command in commands:
        if command[0]=='insert':
            output.insert(int(command[1]),int(command[2]))
        elif command[0]=='print':
            print(output)
        elif command[0]=='append':
            output.append(int(command[1]))
        elif command[0]=='remove':
            output.remove(int(command[1]))
        elif command[0]=='pop':
            output.pop()
        elif command[0]=='sort':
            output.sort()
        elif command[0]=='reverse':
            output.reverse()
    