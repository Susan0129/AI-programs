print("Water jug problem")
x = int(input("Enter x: "))
y = int(input("Enter y: "))
while True:
    rno = int(input("Enter rule: "))
    if rno==1:
        if x<4:
            x=4
    if rno==2:
        if y<3:
            y=3
    if rno==3:
        if x>0:
            d = int(input("Water to be removed: "))
            x = x-d
    if rno==4:
        if y>0:
            d = int(input("Water to be removed: "))
            y = y-d
    if rno==5:
        if x>0:
            x=0
    if rno==6:
        if y>0:
            y=0
    if rno==7:
        if x+y>=4 and y>0:
            x=4
            y=y-(4-x)
    if rno==8:
        if x+y>=3 and x>0:
            x=x-(3-y)
            y=3
    if rno==9:
        if x+y<=4 and y>0:
            x,y=x+y,0
    if rno==10:
        if x+y>=3 and x>0:
            x,y=0,x+y
    print("X=",x)
    print("Y=",y)
    if(x==2):
        print("the result is goal state")
        break