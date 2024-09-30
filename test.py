def sum(a,b):
    if b > 1:
        a += sum(a, b-1)
    return a

def mul(a,b):
    m = sum(a,abs(b))
    if b < 0:
        m = -m
    print(m)


