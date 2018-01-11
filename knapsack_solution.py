import random

numItems = 10
currentSelection = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

values = [2, 9, 8, 5, 4, 0, 2, 7, 5, 3]
weights = [7, 5, 3, 1, 5, 9, 8, 4, 2, 6]
limit = 30

bestValue = 0
bestSelection = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

counter = 0
while(counter < 3000 ):
    counter += 1
    randomItem = random.randint(0, numItems-1)
    if currentSelection[randomItem] == 0:
        currentSelection[randomItem] = 1
    else:
        currentSelection[randomItem] = 0

    for i in range(numItems):
        value = 0
        weight = 0
        for item in range(numItems):
            if currentSelection[item] == 1:
                value += values[item]
                weight += weights[item]
            if (weight <= limit and value > bestValue):
                print(currentSelection, value)
                bestValue = value
                for item in range(numItems):
                    bestSelection[item] = currentSelection[item]

print("best:", bestSelection, bestValue)
