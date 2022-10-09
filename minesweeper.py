from random import Random, randint, random
from re import X


def transform(a):
    for i in range(len(a)):
        for j in range(len(a[i])):
            if a[i][j]==False or a[i][j]==0:
                a[i][j]=0
            else:
                a[i][j]=1
    return a

def summ(x):
    for i in range(len(x)):
        for j in range(len(x[i])):
            p,q=0,0
            
            if x[i][j]==0:
                    pass
            else:
                for k in range(i-1,i+2):
                    for l in range(j-1,j+2):
                        if x[k][l]==0:
                            p+=1
                x[i][j]=p
    return x

def output(a):
    for i in range(len(a)):
        print(a[i])

def click(a,b,x,y,z):
    if a[x][y]==0:
        print("Game Over")
        sub(a)
    else:
        b[x][y]=a[x][y]
        a[x][y]=0
        output(b)
        f=0
        for i in a:
            for j in a:
                if 0==a[i][j]:
                    f+=1
        if f==z:
            print("game won")
        else:
            click(a,b,p=int(input()),q=int(input()))


def table(s):
    l=[]
    for i in range(0,s):
        la=[]
        for j in range(0,s):
            if ((i==0 or j==0) or (i==s-1 or j==s-1)):
                la.append(False)
            else:
                la.append(randint(0,1))
        l.append(la)
    return l

    

def sub(x):
    for i in range(1,len(x)-1):
        for j in range(1,len(x[i])-1):
            print(x[i][j],end=' ')
        print('\n')

def duplicate(s):
    y=[]
    for i in range(0,s):
        ya=[]
        for j in range(0,s):
            ya.append('_')
        y.append(ya)
    return y

while True:
    print("1.Start")
    print("2.Quit")
    s=int(input("Enter "))

    if s==1:
        sa=int(input("Enter more than 3"))
        v=table(sa)
        x=transform(v)
        x=summ(x)
        y=duplicate(sa)
        #sub(x)
        output(y)
        a=int(input("enter position 1"))
        b=int(input("enter position 2"))
        click(x,y,a,b,sa*sa)




