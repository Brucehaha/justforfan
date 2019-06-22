def repeatimes(arrayList):
    """
    [1, 2,2, 3,3,3], count=max=1, arrayList[1]=2>arrayList[1]=1, so count=1, max=1, 2=2, so count=2, 2>max=1, max=2
    :param arrayList:
    :return: max repeated number
    """
    initial = arrayList[0]
    arrayList.sort()
    print(arrayList)
    count=max=1
    maxValue = None
    for i in range(1,len(arrayList)):
        if arrayList[i] == initial:
            count += 1
            if count > max:
                max=count
                maxValue = initial
        else:
            count = 1
            initial = arrayList[i]
    return maxValue, max


print(repeatimes([1, 2,2,3,3,3,4,4]))