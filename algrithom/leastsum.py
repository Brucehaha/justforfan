import sys
def gettwoelementsclosesttozero(myarray):
    arrayLen = len(myarray)
    myarray.sort()
    if arrayLen < 2:
        return False
    left = 0
    right = arrayLen - 1
    minimumLeft = left
    minimumRight = arrayLen - 1
    minimumSum = sys.maxsize
    while(left < right):
        sum = myarray[left] + myarray[right]
        if(abs(minimumSum) > abs(sum)):
            minimumSum = sum
            minimumLeft = left
            minimumRight = right
        if sum < 0:
            left += 1
        else:
            right -= 1
    print("Finally, the two elements whose sum is minimum are ", myarray[minimumLeft], myarray[minimumRight])

myarray = [12, 70, -10, 50, -80, 85]
gettwoelementsclosesttozero(myarray)