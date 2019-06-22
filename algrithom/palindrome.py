def isPalindrome(str):
    strStack = list()
    for char in str:
        strStack.append(char)
    for char in str:
        if char == strStack.pop():
            palindrome = True
        else:
            palindrome = False
            break
    return palindrome

print(isPalindrome('123d21'))

