def unique(arr):

    unique_list = []
    unique_list2 = []

    a = arr[0]

    for i in arr:
        if i != a:
            unique_list.append(i)
        elif i == a:
            unique_list2.append(i)
    if len(unique_list) == 1:
        print(unique_list)
    if len(unique_list2) == 1:
        print(unique_list2)


unique([1,3,1,1,1,1,1])
