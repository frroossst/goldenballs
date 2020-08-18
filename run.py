import time
import random
ra=rb=rc=rd=0
r1_players=[]
r1_vote=[]
r2_vote=[]
ballpit=[10,50,75,100,200,300,500,750,1000,1200,1500,1800,2000,5000,10000,15000,20000,30000,25000,35000,40000,45000,50000,55000,60000,65000,70000,75000]
print(len(ballpit))
p1=pl2=pl3=pl4=""
p1=input("player one : ")
r1_players.append(p1)
p2=input("player two : ")
r1_players.append(p2)
p3=input("player three : ")
r1_players.append(p3)
p4=input("player four : ")
r1_players.append(p4)
playing_lot=random.sample(ballpit,12)
n=0
while n<4:
    playing_lot.append("KILLER")
    n+=1
#print(playing_lot)
p1_lot=random.sample(playing_lot,4)
for i in playing_lot:
    if i == p1_lot[0]:
        a=playing_lot.index(i)
        playing_lot.pop(a)
for i in playing_lot:
    if i == p1_lot[1]:
        a=playing_lot.index(i)
        playing_lot.pop(a)
for i in playing_lot:
    if i == p1_lot[2]:
        a=playing_lot.index(i)
        playing_lot.pop(a)
for i in playing_lot:
    if i == p1_lot[3]:
        a=playing_lot.index(i)
        playing_lot.pop(a)
#print("player 1 lot")
#print(p1_lot)
#r1p2
p2_lot=random.sample(playing_lot,4)
for i in playing_lot:
    if i == p2_lot[0]:
        a=playing_lot.index(i)
        playing_lot.pop(a)
for i in playing_lot:
    if i == p2_lot[1]:
        a=playing_lot.index(i)
        playing_lot.pop(a)
for i in playing_lot:
    if i == p2_lot[2]:
        a=playing_lot.index(i)
        playing_lot.pop(a)
for i in playing_lot:
    if i == p2_lot[3]:
        a=playing_lot.index(i)
        playing_lot.pop(a)
#print("player 2 lot")
#print(p2_lot)
#r1p3
p3_lot=random.sample(playing_lot,4)
for i in playing_lot:
    if i == p3_lot[0]:
        a=playing_lot.index(i)
        playing_lot.pop(a)
for i in playing_lot:
    if i == p3_lot[1]:
        a=playing_lot.index(i)
        playing_lot.pop(a)
for i in playing_lot:
    if i == p3_lot[2]:
        a=playing_lot.index(i)
        playing_lot.pop(a)
for i in playing_lot:
    if i == p3_lot[3]:
        a=playing_lot.index(i)
        playing_lot.pop(a)
#print("player 3 lot")
#print(p3_lot)
#r1p4
p4_lot=playing_lot
p4_lot.append("KILLER")
#print("player 4 lot")
#print(p4_lot)
print("arranging balls in two slots")
time.sleep(2)
print("revealing front row for each player")
time.sleep(1)
i=0
print()
print("front row for",p1)
while i<2:
    print(p1_lot[i])
    i+=1
i=0
print()
print("front row for",p2)
while i<2:
    print(p2_lot[i])
    i+=1
i=0
print()
print("front row for",p3)
while i<2:
    print(p3_lot[i])
    i+=1
i=0
print()
print("front row for",p4)
while i<2:
    print(p4_lot[i])
    i+=1
#time.sleep(45)
#backrow for p1
print()
print("all players except",p1,"must look away")
fp1=open(p1,"w")
p1_lotw1=str(p1_lot[2])
p1_lotw2=str(p1_lot[3])
fp1.writelines(p1_lotw1)
fp1.writelines(" | ")
fp1.writelines(p1_lotw2)
fp1.close()
#time.sleep(15)
print(p1,"check the file with your name on it to see the backrow")
p1brow1=input("reveal your first ball : ")
p1brow2=input("reveal your second ball : ")
print("revealing backrow for",p1)
print(p1brow1)
print(p1brow2)
#backrow for p2
print()
print("all players except",p2,"must look away")
fp2=open(p2,"w")
p2_lotw1=str(p2_lot[2])
p2_lotw2=str(p2_lot[3])
fp2.writelines(p2_lotw1)
fp2.writelines(" | ")
fp2.writelines(p2_lotw2)
fp2.close()
#time.sleep(15)
print(p2,"check the file with your name on it to see the backrow")
p2brow1=input("reveal your first ball : ")
p2brow2=input("reveal your second ball : ")
print("revealing backrow for",p2)
print(p2brow1)
print(p2brow2)
#backrow for p3
print()
print("all players except",p3,"must look away")
fp3=open(p3,"w")
p3_lotw1=str(p3_lot[2])
p3_lotw2=str(p3_lot[3])
fp3.writelines(p3_lotw1)
fp3.writelines(" | ")
fp3.writelines(p3_lotw2)
fp3.close()
#time.sleep(15)
print(p3,"check the file with your name on it to see the backrow")
p3brow1=input("reveal your first ball : ")
p3brow2=input("reveal your second ball : ")
print("revealing backrow for",p3)
print(p3brow1)
print(p3brow2)
#backrow for p4
print()
print("all players except",p4,"must look away")
fp4=open(p4,"w")
p4_lotw1=str(p4_lot[2])
p4_lotw2=str(p4_lot[3])
fp4.writelines(p4_lotw1)
fp4.writelines(" | ")
fp4.writelines(p4_lotw2)
fp4.close()
#time.sleep(15)
print(p4,"check the file with your name on it to see the backrow")
p4brow1=input("reveal your first ball : ")
p4brow2=input("reveal your second ball : ")
print("revealing backrow for",p4)
print(p4brow1)
print(p4brow2)
#voting and deliiberation round
print("each player will now have 45 seconds to defend why they should not be voted out")
print(p1,"has the floor for the next 45 seconds")
#time.sleep(45)
print(p2,"has the floor for the next 45 seconds")
#time.sleep(45)
print(p3,"has the floor for the next 45 seconds")
#time.sleep(45)
print(p4,"has the floor for the next 45 seconds")
#time.sleep(45)
#round one voting
print("now the voting round will begin")
print("enter total number of votes for",p1)
p1_vote=int(input())
r1_vote.append(p1_vote)
print("enter total number of votes for",p2)
p2_vote=int(input())
r1_vote.append(p2_vote)
print("enter total number of votes for",p3)
p3_vote=int(input())
r1_vote.append(p3_vote)
print("enter total number of votes for",p4)
p4_vote=int(input())
r1_vote.append(p4_vote)
print(r1_vote)
max_votes_r1=max(r1_vote)
for i in r1_vote:
    if i == max_votes_r1:
        player_elim=r1_vote.index(i)
        if player_elim == 0:
            print(p1,"has been eliminated")
            r1_players.pop(0)
            ra+=1
        elif player_elim == 1:
            print(p2,"has been eliminated")
            r1_players.pop(1)
            rb+=1        
        elif player_elim == 2:
            print(p3,"has been eliminated")
            r1_players.pop(2)
            rc+=1        
        else:
            print(p4,"has been eliminated")
            r1_players.pop(3)
            rd+=1
#print(r1_players)
#round two begins
round2_lot=r1_players
print(round2_lot)
print("round two is beginning")
print("our players for round 2 are :")
for i in r1_players:
    print(i)
print()
r2p1=round2_lot[0]
r2p2=round2_lot[1]
r2p3=round2_lot[2]
r2_playing_lot=[r2p1,r2p2,r2p3]
#print(r2_playing_lot)
r2_ballpit=[]
r2_ballpit2=[]
r2_ballpit.append(p1_lot)
r2_ballpit.append(p2_lot)
r2_ballpit.append(p3_lot)
r2_ballpit.append(p4_lot)
print(r2_ballpit)
for m in r2_ballpit:   
    for n in m:  
        r2_ballpit2.append(n)
print(r2_ballpit2)
print(len(r2_ballpit2))
if ra == 1 :
    r2_ballpit2.pop(0)
    r2_ballpit2.pop(0)
    r2_ballpit2.pop(0)
    r2_ballpit2.pop(0)
elif rb == 1:
    r2_ballpit2.pop(4)
    r2_ballpit2.pop(4)
    r2_ballpit2.pop(4)
    r2_ballpit2.pop(4)
elif rc == 1:
    r2_ballpit2.pop(8)
    r2_ballpit2.pop(8)
    r2_ballpit2.pop(8)
    r2_ballpit2.pop(8)
elif rd == 1:
    r2_ballpit2.pop(12)
    r2_ballpit2.pop(12)
    r2_ballpit2.pop(12)
    r2_ballpit2.pop(12)
print()
print(r2_ballpit2)
print(len(r2_ballpit2))
r2_ballpit2.append(ballpit[0])
r2_ballpit2.append(ballpit[20])
r2_ballpit2.append('KILLER')
print()
print(r2_ballpit2)
print(len(r2_ballpit2))
r2_ballpit3=random.sample(r2_ballpit2,15)
r2p1_li=[]
r2p2_li=[]
r2p3_li=[]
n=0
while n<5:
    r2p1_li.append(r2_ballpit3[n])
    n+=1
print(r2p1_li)
m=0
while m<5:
    r2p2_li.append(r2_ballpit3[m+5])
    m+=1
print(r2p2_li)
o=0
while o<5:
    r2p3_li.append(r2_ballpit3[o+10])
    o+=1
#front row for p1 for round 2
print(r2p3_li) 
print("front row for",r2p1)
print(r2p1_li[0])
print(r2p1_li[1])
#backrow for p1 for round 2 
print()
print("all players except",p1,"must look away")
fp1r2=open(p1,"w")
p1_lotw1=str(r2p1_li[2])
p1_lotw2=str(r2p1_li[3])
p1_lotw3=str(r2p1_li[4])
fp1r2.writelines(p1_lotw1)
fp1r2.writelines(" | ")
fp1r2.writelines(p1_lotw2)
fp1r2.writelines(" | ")
fp1r2.writelines(p1_lotw3)
fp1r2.close()
#front row for p2 for round 3
print("front row for",r2p2)
print(r2p2_li[0])
print(r2p2_li[1])
#backrow for p2 for round 2
print()
print("all players except",p2,"must look away")
fp2r2=open(p2,"w")
p2_lotw1=str(r2p2_li[2])
p2_lotw2=str(r2p2_li[3])
p2_lotw3=str(r2p2_li[4])
fp2r2.writelines(p2_lotw1)
fp2r2.writelines(" | ")
fp2r2.writelines(p2_lotw2)
fp2r2.writelines(" | ")
fp2r2.writelines(p2_lotw3)
fp2r2.close()
#front row for p3 for round 3
print("front row for",r2p3)
print(r2p3_li[0])
print(r2p3_li[1])
#backrow for p3 for round 2
print()
print("all players except",p3,"must look away")
fp3r2=open(p3,"w")
p3_lotw1=str(r2p3_li[2])
p3_lotw2=str(r2p3_li[3])
p3_lotw3=str(r2p3_li[4])
fp3r2.writelines(p3_lotw1)
fp3r2.writelines(" | ")
fp3r2.writelines(p3_lotw2)
fp3r2.writelines(" | ")
fp3r2.writelines(p3_lotw3)
fp3r2.close()
#voting and deliberation round
print("each player will now have 45 seconds to defend why they should not be voted out")
print(r2p1,"has the floor for the next 45 seconds")
#time.sleep(45)
print(r2p2,"has the floor for the next 45 seconds")
#time.sleep(45)
print(r2p3,"has the floor for the next 45 seconds")
#time.sleep(45)
#voting for round two
print("now the voting round will begin")
print("enter total number of votes for",r2p1)
p1_vote=int(input())
r2_vote.append(p1_vote)
print("enter total number of votes for",r2p2)
p2_vote=int(input())
r2_vote.append(p2_vote)
print("enter total number of votes for",r2p3)
p3_vote=int(input())
r2_vote.append(p3_vote)
print(r2_vote)
r2v=0
round3_lot=[]
r2v_max=max(r2_vote)
r2v_ind=r2_vote.index(r2v_max)    
print()
print(r2v_max)
print(r2v_ind)
print()
print(round2_lot)
print(round2_lot.pop(r2v_ind))
print(round2_lot)
print("ballpit r2")
print(r2_ballpit2)
round3_lot=round2_lot
print(round3_lot[0],"and",round3_lot[1],"will head into the final round")
print("round 3 ... bin or win")
bin_li=[]
win_li=[]
prize_pool=0
print(len(r2_ballpit2))
if r2p1 not in round3_lot:
    r2_ballpit2.pop(0)
    r2_ballpit2.pop(0)
    r2_ballpit2.pop(0)
    r2_ballpit2.pop(0)
    r2_ballpit2.pop(0)
elif r2p2 not in round3_lot:
    r2_ballpit2.pop(5)
    r2_ballpit2.pop(5)
    r2_ballpit2.pop(5)
    r2_ballpit2.pop(5)
    r2_ballpit2.pop(5)
elif r2p3 not in round3_lot:
    r2_ballpit2.pop(10)
    r2_ballpit2.pop(10)
    r2_ballpit2.pop(10)
    r2_ballpit2.pop(10)
    r2_ballpit2.pop(10)
print(r2_ballpit2)
r3_ballpit=r2_ballpit2
r3_ballpit.append("KILLER")
prize_pool=[]
prize_pot=0
balls=['BALL','BALL','BALL','BALL','BALL','BALL','BALL','BALL','BALL','BALL','BALL ']
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
print("prize pool : ",prize_pot)
#split or steal
r3p1=round3_lot[0]
r3p2=round3_lot[1]
print("each player will no vote split or steal")
print("if both people split the prize pool is divided into half")
print("if both people steal none of them get the prize pool")
print("if one of you split and the other steal the latter gets the entire prize pool")
print("you now have 60 seconds to deliberate with each other")
#time.sleep(60)
print("enter 1 to steal and 0 to split")
print("now",r3p1,"will vote")
v1=int(input("please enter your vote : "))
print("now",r3p2,"will")
v2=int(input("please enter your vote : "))
if v1==0 and v2==0:
    print("both of you have won",prize_pot//2)
    print("sharing is caring afterall")
elif v1==1 and v2==1:
    print("looks like you're taking home 0 dollars")
    print("There is no fire like passion, there is no shark like hatred, there is no snare like folly, there is no torrent like greed.\n ― Siddharta Gautama ")
elif v1 != v2:
    if v1<v2:
        print("***",r3p1,"***")
        print("you are the proud owner of",prize_pool)
        print("If you steal something small you are a petty thief, but if you steal millions you are a gentleman of society.")
    elif v2>v1:
        print("***",r3p2,"***")
        print("has just stolen",prize_pool)
        print("You shall not steal, nor deal falsely, nor lie to one another. -moses")












