class piece:
    def __init__(self,x,y,z,c1,c2,c3):
        self.x=x
        self.y=y
        self.z=z
        self.c1=c1
        self.c2=c2
        self.c3=c3
def R_turn(a):
    blist=[]
    for q in range(1,-1,-1):
        clist=[]
        for w in range(2):
            y=a[w][q][1].c1
            a[w][q][1].c1=a[w][q][1].c2
            a[w][q][1].c2=y
            clist.append(a[w][q][1])
        blist.append(clist)
    for q in range(2):
        for w in range(2):
            a[q][w][1]=blist[q][w]
    return a
def L_turn(a):
    blist=[]
    for q in range(2):
        clist=[]
        for w in range(1,-1,-1):
            y=a[w][q][0].c1
            a[w][q][0].c1=a[w][q][0].c2
            a[w][q][0].c2=y
            clist.append(a[w][q][0])
        blist.append(clist)
    for q in range(2):
        for w in range(2):
            a[q][w][0]=blist[q][w]
    return a
def U_turn(a):
    blist=[]
    for q in range(2):
        clist=[]
        for w in range(1,-1,-1):
            y=a[0][w][q].c2
            a[0][w][q].c2=a[0][w][q].c3
            a[0][w][q].c3=y
            clist.append(a[0][w][q])
        blist.append(clist)
    for q in range(2):
        for w in range(2):
            a[0][q][w]=blist[q][w]
    return a
def D_turn(a):
    blist=[]
    for q in range(1,-1,-1):
        clist=[]
        for w in range(2):
            y=a[1][w][q].c2
            a[1][w][q].c2=a[1][w][q].c3
            a[1][w][q].c3=y
            clist.append(a[1][w][q])
        blist.append(clist)
    for q in range(2):
        for w in range(2):
            a[1][q][w]=blist[q][w]
    return a
def F_turn(a):
    blist=[]
    for q in range(2):
        clist=[]
        for w in range(1,-1,-1):
            y=a[w][1][q].c1
            a[w][1][q].c1=a[w][1][q].c3
            a[w][1][q].c3=y
            clist.append(a[w][1][q])
        blist.append(clist)
    for q in range(2):
        for w in range(2):
            a[q][1][w]=blist[q][w]
    return a
def B_turn(a):
    blist=[]
    for q in range(1,-1,-1):
        clist=[]
        for w in range(2):
            y=a[w][0][q].c1
            a[w][0][q].c1=a[w][0][q].c3
            a[w][0][q].c3=y
            clist.append(a[w][0][q])
        blist.append(clist)
    for q in range(2):
        for w in range(2):
            a[q][0][w]=blist[q][w]
    return a
alist=[]
for q in range(2):
    if q==0:
        a="w"
    else:
        a="y"
    blist=[]
    for w in range(2):
        if w==0:
            b="b"
        else:
            b="g"
        clist=[]
        for e in range(2):
            if e==0:
                c="o"
            else:
                c="r"
            clist.append(piece(q,w,e,a,b,c))
        blist.append(clist)
    alist.append(blist)
for q in range(2):
    for w in range(2):
        if w==1:
            print(alist[0][q][w].c1)
        else:
            print(alist[0][q][w].c1,end=" ")
for q in range(2):
    for w in range(2):
        for e in range(2):
            print(alist[q][1-w][abs(w-e)].c2,end=" ")
        for e in range(2):
            if w+e==2:
                print(alist[q][abs((1-w)-e)][1-w].c3)
            else:
                print(alist[q][abs((1-w)-e)][1-w].c3,end=" ")
for q in range(2):
    for w in range(4):
        print(" ",end=" ")
    for w in range(1,-1,-1):
        if w==0:
            print(alist[1][q][w].c1)
        else:
            print(alist[1][q][w].c1,end=" ")
q=1
while q==1:
    i=input("")
    if len(i)==1:
        if i=="R":
            alist=R_turn(alist)
        elif i=="L":
            alist=L_turn(alist)
        elif i=="U":
            alist=U_turn(alist)
        elif i=="D":
            alist=D_turn(alist)
        elif i=="F":
            alist=F_turn(alist)
        elif i=="B":
            alist=B_turn(alist)
        elif i=="x":
            alist=R_turn(L_turn(L_turn(L_turn(alist))))
        elif i=="y":
            alist=U_turn(D_turn(D_turn(D_turn(alist))))
        elif i=="z":
            alist=F_turn(B_turn(B_turn(B_turn(alist))))
        else:
            print("Invalid move")
    elif len(i)==2:
        if i[1]=="2":
            if i[0]=="R":
                alist=R_turn(R_turn(alist))
            elif i[0]=="L":
                alist=L_turn(L_turn(alist))
            elif i[0]=="U":
                alist=U_turn(U_turn(alist))
            elif i[0]=="D":
                alist=D_turn(D_turn(alist))
            elif i[0]=="F":
                alist=F_turn(F_turn(alist))
            elif i[0]=="B":
                alist=B_turn(B_turn(alist))
            elif i=="x":
                alist=R_turn(R_turn(L_turn(L_turn(alist))))
            elif i=="y":
                alist=U_turn(U_turn(D_turn(D_turn(alist))))
            elif i=="z":
                alist=F_turn(F_turn(B_turn(B_turn(alist))))
            else:
                print("Invalid move")
        elif i[1]=="'":
            if i[0]=="R":
                alist=R_turn(R_turn(R_turn(alist)))
            elif i[0]=="L":
                alist=L_turn(L_turn(L_turn(alist)))
            elif i[0]=="U":
                alist=U_turn(U_turn(U_turn(alist)))
            elif i[0]=="D":
                alist=D_turn(D_turn(D_turn(alist)))
            elif i[0]=="F":
                alist=F_turn(F_turn(F_turn(alist)))
            elif i[0]=="B":
                alist=B_turn(B_turn(B_turn(alist)))
            elif i=="x":
                alist=R_turn(R_turn(R_turn(L_turn(alist))))
            elif i=="y":
                alist=U_turn(U_turn(U_turn(D_turn(alist))))
            elif i=="z":
                alist=F_turn(F_turn(F_turn(B_turn(alist))))
            else:
                print("Invalid move")
        else:
            print("Invalid move")
    elif i=="stop":
        q=q+1
    elif i=="solve":
        print("Solve function not yet implemented")
    else:
        print("Invalid move")
    for w in range(2):
        for e in range(2):
            if e==1:
                print(alist[0][w][e].c1)
            else:
                print(alist[0][w][e].c1,end=" ")
    for w in range(2):
        for e in range(2):
            for r in range(2):
                print(alist[w][1-e][abs(e-r)].c2,end=" ")
            for r in range(2):
                if e+r==2:
                    print(alist[w][abs((1-e)-r)][1-e].c3)
                else:
                    print(alist[w][abs((1-e)-r)][1-e].c3,end=" ")
    for w in range(2):
        for e in range(4):
            print(" ",end=" ")
        for e in range(1,-1,-1):
            if e==0:
                print(alist[1][w][e].c1)
            else:
                print(alist[1][w][e].c1,end=" ")


