'''arm strong number'''


num=int(input("Enter a number:"))
copy= num
s=0
while num!=0:
    r=num%10
    s+=r*r*r
    num//=10
if copy==s:
    print(copy,"is an arm storng number:")
else:
    print(copy,"is not an arm strong number")



'''nivens'''

num=int(input("Enter a number:"))
copy=num
s=0
while num!=0:
    r=num%12
    num//10

if copy==s:
    print(copy,"is an nivens number:")
else:
    print(copy,"is not an nivens number:")



'''factorail'''

num=int(input("Enter a number:"))
fact=1
i=1
while i<num:
    fact*=i
    i+=1
print(fact)       
