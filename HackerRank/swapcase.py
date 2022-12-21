def swap_case(s):
    
    output=""
    for i in s:
        if i.islower():
            output+=i.upper()
        else:
            output+=i.lower()
    return output

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)