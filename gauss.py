def printMat(matrix):
    for i in range(len(matrix)):
        print(matrix[i])
    print("")

def gaussJordan(a):
    for index in range(len(a)):
        print("processing column", index)

        if(a[index][index] == 0):
            print("step 1: swap")
            swapWith = 0
            for swapWith in range(len(a)):
                if a[swapWith][index] != 0:
                    tempSwap = a[index]
                    a[index] = a[swapWith]
                    a[swapWith] = tempSwap
                    break

        value_at_index = a[index][index]
        if value_at_index != 1:
            print("step2: normalization")
            for j in range(len(a[index])):
                a[index][j]

        print("step3: replacemaent")
        for i in range(len(a)):
            if(i != index):
                multiplier = a[i][index]
                for j in range(len(a[i])):
                    a[i][j] = a[i][j] - multiplier*a[index][j]

        printMat(a)
    return a[0][3], a[1][3], a[2][3]

input_mat = [[1, 1, 1, 3],
            [2, 3, 7, 0],
            [1, 3, -2, 17]]

printMat(input_mat)
[x,y,z] = gaussJordan(input_mat)
print("x",x, "y",y, "z",z)
