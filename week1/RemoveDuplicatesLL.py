class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insert(self, data):
        newnode = Node(data)
        if self.head is None:
            self.head = newnode
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = newnode

    def display(self):
        current = self.head
        while current:
            print(current.data, end=" ")
            current = current.next
        print()

    def removeDuplicate(self):
        if self.head is None:
            return None
        
        current = self.head
        while current and current.next:
            if current.data == current.next.data:
                current.next = current.next.next
            else:
                current = current.next
        return self.head

ll = LinkedList()
n = int(input())
arr = list(map(int, input().split()))
for i in range(n):
    ll.insert(arr[i])
ll.removeDuplicate()
ll.display()