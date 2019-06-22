def findrepeate(arrayList):
    for i in range(0, len(arrayList)):
        if arrayList[abs(arrayList[i])] < 0:
            return abs(arrayList[i])
        else:
            arrayList[abs(arrayList[i])] = -arrayList[abs(arrayList[i])]
    return "no repeate"



print(findrepeate([3,2,4,1,4]))