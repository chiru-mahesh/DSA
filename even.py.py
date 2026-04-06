#write a code to print all even n natural numbers

n=int(input("enter a value of n:"))
i=1
while i<=n:
    if i%2==0:
        print(i, end=" ")
    
    i+=1
