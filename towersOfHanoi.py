def towerOfHanoi(n,f,t,a,from_rod,to_rod,aux_rod):
    if n==1:
        print("move disk 1 from ",from_rod,"to rod", to_rod)
        t.append(1)
        f.remove(1)
        print(from_rod,': ',f,' ',aux_rod,': ',a,' ',to_rod,': ',t)
        return
    towerOfHanoi(n-1,f,a,t,from_rod,aux_rod,to_rod)
    print("move disk ",n," from ",from_rod,"to rod", to_rod)
    t.append(n)
    f.remove(n)
    print(from_rod,': ',f,' ',aux_rod,': ',a,' ',to_rod,': ',t)
    towerOfHanoi(n-1,a,t,f,aux_rod,to_rod,from_rod)
n=4
A=[4,3,2,1]
B=[]
C=[]
towerOfHanoi(n,A,C,B,'A','C','B')