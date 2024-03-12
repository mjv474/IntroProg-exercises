def myfun(n):
    for i in range(n):
        print('hello world!')

def simple_g(x, omega):
    if x <= omega and x >= - omega:
        return x
    elif x < - omega:
        return -omega
    elif x > omega:
        return omega
    else:
        print("error")