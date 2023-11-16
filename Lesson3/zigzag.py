import time,sys
n=int(input())
change=True
indent=0
while True:
    print(' '*indent,end=" ")
    print('******')
    time.sleep(0.1)
    if change==True:
        indent+=1
        if indent==n:
            change=False
    else:
        indent-=1
        if indent==0:
            change=True
