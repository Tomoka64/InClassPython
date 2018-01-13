dist = [[-1, 4, 5, 7],
[4, -1, 3, 2],
[5, 3, -2, 6],
[7, 2, 6, -1]]

currentCity = 0

visitedCities = [0]

numCities = 4

while len(visitedCities) <numCities:
    #find min
    minCost = 100
    minCity = -1
    for destinationCity in range (numCities):
        if dist[currentCity][destinationCity] < minCost and dist[currentCity][destinationCity] >0:
            minCity = destinationCity
            minCost = dist[currentCity][destinationCity]

    #mark as visited
    visitedCities.append(minCity)
    dist[currentCity][minCity] = -1
    dist[minCity][currentCity]= -1

    currentCity = minCity

print(visitedCities)
