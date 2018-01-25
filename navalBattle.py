import random
myBoard = [[0, 0, 0, 1, 0], [0, 0, 1, 0, 0], [0, 0, 1, 0, 0], [0, 0, 0, 0, 0],
[1, 0, 0, 0, 1]]
enemysBoard = [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0,
0], [0, 0, 0, 0, 0]]
enemyShips = 0
while True:
    x = random.randint(0,4)
    y = random.randint(0,4)
    if enemysBoard[x][y]==0:
        enemysBoard[x][y]=1
        print("Assigning a ship to coordinates ", x, y)
        enemyShips += 1
    if enemyShips == 5:
        break
    for i in range (5):
        print(myBoard[i])
print()
for i in range (5):
    print(enemysBoard[i])
