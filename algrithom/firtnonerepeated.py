def firstNoneRepeated(arrayList):
    """
    1, dict = {}
    2, for item in [1,1, 2, 3], if dict[item], then dict[item] += 1, else: dict[item]=1

    :param arrayList:
    :return: first non repeated number
    """

    dict = {}
    for x in arrayList:
        if x in dict:
            dict[x] += 1
        else:
            dict[x] = 1
    for x in dict:
        if dict[x] == 1:
            return "the first value is %s" % x



print(firstNoneRepeated([1,1, 2, 3]))