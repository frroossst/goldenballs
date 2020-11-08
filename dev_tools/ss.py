prize_pot=50000
r3p1='player one'
r3p2='player two'
print("each player will now vote split or steal")
print("if both people split the prize pool is divided into half")
print("if both people steal none of them get the prize pool")
print("if one of you split and the other steal the latter gets the entire prize pool")
print("you now have 60 seconds to deliberate with each other")
print("enter 1 to steal and 0 to split")
print("now",r3p1,"will vote")
v1=int(input("please enter your vote : "))
print("now",r3p2,"will vote")
v2=int(input("please enter your vote : "))
if v1==0 and v2==0:
    print("both of you have won",prize_pot//2)     
    print("sharing is caring afterall")
elif v1==1 and v2==1:
    print("looks like you're taking home 0 dollars")
    print("There is no fire like passion, there is no shark like hatred, there is no snare like folly, there is no torrent like greed.\n ― Siddharta Gautama ")
elif v1 != v2:
    if v1<v2:
        print("***",r3p2,"***")
        print("you are the (not so) proud owner of",prize_pot)
        print("If you steal something small you are a petty thief, but if you steal millions you are a gentleman of society.")
    elif v1>v2:
        print("***",r3p1,"***")
        print("has just stolen",prize_pot)
        print("You shall not steal, nor deal falsely, nor lie to one another. -moses")

