class Node():
    def __init__(self,data):
        self.data = data 
        self.next = None   

class LinkedList():
    def __init__(self):
        self.head = None
    def add_data(self,data):
        newNode = Node(data)
        if not self.head:
            self.head = newNode
        else:
            temp = self.head
            while(temp.next!=None):
                temp = temp.next
            temp.next = newNode
    def display(self):
            if not self.head:
                print("not in linked list")
                return
            temp = self.head
            while(temp):
                print(temp.data,end="->")
                temp = temp.next
    
    def delete(self,a):
        if self.head == None:
            print("not in list")
            return
        elif(a==1):
            temp = self.head
            self.head = temp.next
        else:
            prev = None
            current = self.head
            for i in range(1,a):
                prev = current
                current = current.next
            prev.next = current.next
            

#first creat a linked list
l = LinkedList()
l.add_data(2)
l.add_data(3)
l.delete(2)
l.display()
