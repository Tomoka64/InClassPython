import random

numItems = 10
numChromosomes = 10

values = [2, 9, 8, 5, 4, 0, 2, 7, 5, 3]
weights = [7, 5, 3, 1, 5, 9, 8, 4, 2, 6]

limit = 30

population = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]

fitness = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

for c in range(numChromosomes):
    for j in range(numItems):
        population[c][j] = random.randint(0, 1)

#print(population, "\n")

for c in range(numChromosomes):
    value = 0
    weight = 0
    for item in range(numItems):
        if population[c][item] == 1:
            value += values[item]
            weight += weights[item]
    if weight <= limit:
        fitness[c] = value
        population = fitness[c]
        print(fitness)


#select one best chromosome and 1 random chromosome to be parents
bestChromosome = -1
bestFitness = -1
for c in range(numChromosomes):
    if fitness[c] > bestFitness:
        bestFitness = fitness[c] #max
        bestChromosome = c #argmax

while (randomeChromosome == bestChromosome):
    randomChromosome = random.randint(0, numChromosomes-1)


#or you could do
    #randomeChromosome = randome.randint(0, numChromosomes-1)

    #bestChromosome = -1
    #bestFitness = -1
    # for c in range(numChromosomes):
    #     if fitness[c] > bestFitness and c != randomChromosome:
    #         bestFitness = fitness[c] #max
    #         bestChromosome = c #argmax
parent1 = population[bestChromosome ]
parent2 = population[randomChromosome]



#one best crossover at half point
child1 = []
child2 =[]
for i in range(numItems):
    if i < numItems/2:
        child1.append(parent1[i])
        child2.append(parent2[i])
    else:
        child2.append(parent1[i])
        child1.append(parent2[i])

#bit flip mutation

randomItem = random.randint(0, numItems-1)
child1[randomItem] = int(not child1[randomItem])
randomItem = random.randint(0, numItems-1)
child2[randomItem] = int(not child2[randomItem])

print(parent1)
print(parent2)
print(child1)
print(child2)
mu
