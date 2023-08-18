if __name__ == '__main__':
    s = input()
    i = 0
    for letter in s:
        if letter.isalnum():
            print(True)
            break
        elif i == len(s)-1:
            print(False) 
        i += 1
    i = 0
    for letter in s:
        if letter.isalpha():
            print(True)
            break
        elif i == len(s)-1:
            print(False) 
        i += 1
    i = 0
    for letter in s:
        if letter.isdigit():
            print(True)
            break
        elif i == len(s)-1:
            print(False) 
        i += 1
    i = 0
    for letter in s:
        if letter.islower():
            print(True)
            break
        elif i == len(s)-1:
            print(False) 
        i += 1
    i = 0
    for letter in s:
        if letter.isupper():
            print(True)
            break
        elif i == len(s)-1:
            print(False) 
        i += 1