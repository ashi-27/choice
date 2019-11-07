from random import choice
players = ['miley','tom','harry','mike']

teamA=[]
teamB=[]

print(players)


while len(players)>0:
    playerA = choice(players) 
    teamA.append(playerA)
    players.remove(playerA)


    playerB = choice(players)
    teamB.append(playerB)
    players.remove(playerB)


print("teamA=",teamA)

print("teamB=",teamB)
