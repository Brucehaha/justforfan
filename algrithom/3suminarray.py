def get3(array, sum):
    array.sort()
    size = len(array)
    left = 0
    right = size-1
    # iterate array,
    numbers=[]
    for x in range(0, size-2):
        left = x+1
        right = size -1
        while left < right:
            if array[x]+array[left]+array[right] == sum:
                numbers.append([array[x],array[left], array[right]])
                left += 1
                right -= 1
            if array[x]+array[left]+array[right] < sum:
                left += 1
            else:
                right -= 1
    return numbers

myarray = [22, 6, 45, 40, 10, 18, 21]
print(get3(myarray, 72))