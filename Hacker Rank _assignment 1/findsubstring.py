def count_substring(string, sub_string):
    lis = [string[i:j] for i in range(len(string)) for j in range(i + 1, len(string)+1)]
    return lis.count(sub_string)

if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    
    count = count_substring(string, sub_string)
    print(count)
