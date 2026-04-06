'''program to reverse the words in a string'''

words=input("Enter words:").split()
for word in words:
    print(word[::-1],end=" ")