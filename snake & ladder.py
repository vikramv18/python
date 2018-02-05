import random
count=0
while(count<=100):
    roll=input("press r to roll the dice")
    if(roll=='r'):
        r=random.randint(1,6)
        count=count+r
        print("your random number is",r)
        print("you are in position",count)
        if count==8:
            count==37
            print("climb ladder",count)
        elif count==11:
            count==2
            print("snake is bitten so getdown",count)
        elif count==13:
            count=34
            print("climb ladder",count)
        elif count==25:
            count=4
            print("snake is biten so getdown",count)
        elif count==38:
            count=9
            print("snake is bitten so getdown",count)
        elif count==40:
            count==68
            print("climb ladder",count)
        elif count==52:
            count==81
            print("climb ladder",count)
        elif count==65:
            count==46
            print("snake is bitten so getdown",count)
        elif count==76:
            count==97
            print("climb ladder",count)
        elif count==89:
            count==70
            print("climb ladder",count)
        elif count==93:
            count==64
            print("snake is bitten so getdown",count)
        elif(count>100):
            count=count-r
            print("stay back at",count)
        elif count==100:
            print("Congratulations,you won the game")
            break
