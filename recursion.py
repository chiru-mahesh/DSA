'''recursion'''

def nums(n):
    if n==0:
        return
    print(n,end=" ")
    nums(n-1)
n=int(input("Enter a number:"))
nums(n)   

#task1

def nums(n):
    if n==11:
        return
    print(n,end=" ")
    nums(n+1)
n=int(input("Enter a number:"))
nums(n)    