import random
t = list()

for i in range(1,3):
    s = input("enter team name ")
    t.append(s)

print(t)
team1 = list()
team2 = list()

toss = random.randrange(1,101)
if(toss%2==0):
    print(t[0], "bat first")
    for i in range (1,12):
        team1.append(random.randrange(1,101))
    print(t[1], "bat second")
    for i in range (1,12):
        team2.append(random.randrange(1,101))
    
else:
    print(t[1], "bat first")
    for i in range (1,12):
        team2.append(random.randrange(1,101))
    print(t[0], "bat second")
    for i in range (1,12):
        team1.append(random.randrange(1,101))
    
        

#print(team1)
#print(team2)

for i in range(11):
    print("Player ", i+1, team1[i], end="\t")
    print("Player ", i+1, team2[i])

print("Total run by",t[0],sum(team1))
print("Total run by",t[1],sum(team2))
if (sum(team1) - sum(team2))>0:
    print(t[0], "win by ", sum(team1) - sum(team2), "runs")
else:
    print(t[1], "win by", sum(team2) - sum(team1), " runs")

mom =  max(team1) if max(team1) > max(team2) else max(team2)
print("Man of the match", mom)