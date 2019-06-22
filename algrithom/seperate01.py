def seperate(array):
    left=0
    right = len(array)-1
    while left < right:
        while array[left] == 1 and left < right:
            left += 1
        while array[right]== 0 and left < right:
            right -= 1
        if left < right:
            array[left], array[right]=array[right], array[left]
            left += 1
            right -= 1

    return array
        
        
        
print(seperate([1,0,1,0,1,1,1,1]))