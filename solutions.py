from collections import Counter

def question1(s, t):
    s_count = Counter(s)
    t_count = Counter(t)
    s_count.subtract(t_count)
    for x in s_count.values():
        if x < 0:
            return False
    return True
