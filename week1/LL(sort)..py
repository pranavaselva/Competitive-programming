class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insert(self, data):
        newNode = Node(data)
        if self.head is None:
            self.head = newNode
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = newNode

    def display(self):
        current = self.head
        while current:
            print(current.data, end=" ")
            current = current.next
        print()

    def sorting(self):
        count = [0, 0, 0]

        current = self.head
        while current:
            count[current.data] += 1
            current = current.next

        current = self.head
        i = 0
        while current:
            if count[i] == 0:
                i += 1
            else:
                current.data = i
                count[i] -= 1
                current = current.next

ll = LinkedList()
n = int(input())
arr = list(map(int, input().split()))
for i in range(n):
    ll.insert(arr[i])
ll.sorting()
ll.display()