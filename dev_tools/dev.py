prize_pool=[]
prize_pot=0
balls=['BALL','BALL','BALL','BALL','BALL','BALL','BALL','BALL','BALL','BALL','BALL ']
r3_ballpit=['KILLER',1000,200,20,10,2000,5000,'KILLER',750,50000,'KILLER']
i=0
while i < 5:
    print(balls)
    bin0=int(input("enter a ball to be binned : "))
    r3_ballpit.pop(bin0-1)
    balls.pop(bin0-1)
    print(balls)
    win0=int(input("enter a ball to add to the prize pool : "))
    prize_pool.append(r3_ballpit[win0-1])
    r3_ballpit.pop(win0-1)
    balls.pop(win0-1)
    print(balls)
    i+=1
print()
if prize_pool[0]=='KILLER':
    prize_pool.pop(0)
print()
for i in prize_pool:
    if (str(i)).isalpha():
        prize_pot=prize_pot//10
    else:
        prize_pot+=i
print(prize_pot)
