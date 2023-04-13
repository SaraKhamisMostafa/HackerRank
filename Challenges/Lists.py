def Lists():
    N = int(input())
    newList=[]
    for i in range(N):
        cmd=input().split()
        if cmd[0]=='insert':
            newList.insert(int(cmd[1]),int(cmd[2]))    
        if cmd[0] == 'print':    
            print(newList)
        if cmd[0]=='remove':
            newList.remove(int(cmd[1])) 
        if cmd[0]=='append':
            newList.append(int(cmd[1]))
        if cmd[0]=='sort':
           newList.sort()
        if cmd[0]=='pop':
           newList.pop()
        if cmd[0]=='reverse':
           newList.reverse()                                   
Lists()
