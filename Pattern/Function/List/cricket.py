t1 = []
t2 = []

for i in range(1,12):
    x = int(input("Enter run T1of player no {} :".format(i)))
    t1.append(x)

for i in range(1,12):
    x = int(input("Enter run of T2 player no {} :".format(i)))
    t2.append(x)


print("Total run of team no. 1 ",t1)
print("Total run of team no. 2 ",t2)

win =  sum(t1) - sum(t2)

if (win > 0):
    print("team 1 win by {} run".format(win))
elif(win < 0):
    print("team 2 win by {} run".format(abs(win)))
else:
    print("Game barabri ka hua tha")
print(t1.count(0))
print(t2.count(0))

  