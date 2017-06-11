from collections import Counter

def question1(s, t):
    s_count = Counter(s)
    t_count = Counter(t)
    s_count.subtract(t_count)
    for x in s_count.values():
        if x < 0:
            return False
    return True

def question2(string):
    length = len(string)
    max_length = 1
    start = 0
    table = [[False for x in string] for x in string]
    for x in range(length):
        table[x][x] = True
    for x in range(length - 1):
        if string[x] == string[x+1]:
            table[x][x+1] = True
            start = x
            max_length = 2
    for sub_length in range(3, length + 1):
        for x in range(length - sub_length + 1):
            end = x + sub_length - 1
            if table[x+1][end-1] and string[x] == string[end]:
                table[x][end] = True
                if sub_length > max_length:
                    start = x
                    max_length = sub_length
    return string[start:start+max_length]
    