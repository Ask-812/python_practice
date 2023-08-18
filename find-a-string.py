def count_substring(string, sub_string):
    counter = 0
    for i in range(len(string)-len(sub_string)+1):
        temp = string[i:i+len(sub_string)]
        print(temp)
        if temp == sub_string:
            counter += 1
    return counter

if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    
    count = count_substring(string, sub_string)
    print(count)