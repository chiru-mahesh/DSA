'''write a code to add the sum  of digits of agiven number'''

n=int(input("enter a number:"))
s=0
while n!=0:
    r=n%10
    s+=r
    n=n//10
print("sum",s)