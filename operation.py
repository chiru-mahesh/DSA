#operations

class node:
    def __init__(self,data):
        self.data=data
        self.next=None
head=None
def insert(data):
    global head
    newnode=node(data)
    newnode.next=head
    head=newnode
def delete(value):
    global head
    temp=head
    if temp and temp.data==value:
        head=temp.next
        return
    prev=None
    while temp and temp.data!=value:
        prev=temp
        temp=temp.next
    if temp is None:
        print("Value not in Linkedlist....😒")
        return
    prev.next=temp.next
    print("Deleted value:",value) 
def display():
    temp=head
    while temp:
        print(temp.data,end="->")
        temp=temp.next
    print("None")

n=int(input("Enter number of nodes:"))                         
for _ in range(n):
    val=int(input("Enter value:"))
    insert(val)
print("Inserted LinkedList:")
display()
key=int(input("Enter the value of node to be deleted"))
delete(key)
print("\n update LinkedList:")
display()    