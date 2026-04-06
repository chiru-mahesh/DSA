'''max value'''

arr=list(map(int,input("Enter the numbers:").split()))  # 1 2 3 4
max_value= arr[0]
for i in arr:
    if i>max_value:
        max_value=i
print(max_value)