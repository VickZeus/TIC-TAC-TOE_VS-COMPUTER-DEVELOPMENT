class RGRG :
    def WinTester(self,pa) : # Tests For All The Winning Combinations In The Player String.
        win_patterns = ['A1-A2-A3','B1-B2-B3','C1-C2-C3','A1-B1-C1','A2-B2-C2','A3-B3-C3','A1-B2-C3','A3-B2-C1']
        for i in win_patterns :
            k=i.split('-')
            if ((k[0] in pa) and (k[1] in pa) and (k[-1] in pa)) :
                    return True
        return False
    
    def saver(self,l) :
        import csv
        a=open("Gameplay_History.csv","a",newline="\n")
        w=csv.writer(a)
        w.writerow(l)
        a.close()

    def rand_gen(self) :
        import random
        k=chr(random.randint(65,67))
        n=random.randint(1,3)
        pos=str(k)+str(n)
        return pos
         
    def generator(self) :
            la=["P1 : ",'.','.','.','.','.']
            lb=["P2 : ",'.','.','.','.','.']
            win_list=["D"]
            ca,cb=1,1
            pa,pb="",""
            count=1
            while count<=9 :
                if count%2==0 :
                    flag=True
                    if ca>=3 :
                        if obj.WinTester(pa) :
                            win_list[0]="P1"
                            count=100
                    if count!=100 :
                     while flag :
                        pos=obj.rand_gen()
                        lk=la+lb
                        if pos not in lk :
                            lb[cb]=pos
                            pb+=pos
                            cb+=1
                            flag=False
                            count+=1            
                elif count%2!=0 :
                    flag=True
                    if cb>=3 :
                        if obj.WinTester(pb) :
                            win_list[0]="P2"
                            count=100
                    if  count!=100 :
                     while flag :
                        pos=obj.rand_gen()
                        lk= la+lb
                        if pos not in lk :
                            la[ca]=pos
                            pa+=pos
                            ca+=1
                            flag=False
                            count+=1
            lk=la+lb+win_list
            return lk

    def main(self) :
        k=[]
        l_final=[]
        for i in range(50000) :
            l_final=obj.generator()
            if l_final not in k :
                obj.saver(l_final)
                k.append(l_final)
                print("working...",i)
            else :
                print("Wrong !!!")
        print("Done...")
obj=RGRG()
obj.main()                   
                  

