def func() :
    import csv
    a=open("X:\XO GAME DEVELOPMENT\VS COMPUTER MODE DEVELOPMENT\Gameplay_History.csv",'r')
    r=csv.reader(a)
    p1_c,p2_c,d_c=0,0,0
    total=0
    for i in r :
        total+=1
        if i[-1]=="D" :
            d_c+=1
        elif i[-1]=="P1" :
            p1_c+=1
        elif i[-1]=="P2" :
            p2_c+=1
    print("Player 1 Won >> "+str(p1_c)+"/"+str(total))
    print("Player 2 Won >> "+str(p2_c)+"/"+str(total))
    print("DRAW         >> "+str(d_c)+"/"+str(total))
func()