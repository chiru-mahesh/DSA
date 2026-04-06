'''nested recursion'''


def fun(n):
    if n>10:
        return n-1
    return fun(fun(n+2))
n=int(input("Enter a number:"))
print(fun(n))