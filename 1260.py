maxNum, count, start = map(int,input().split(' '))



class Node:
    def __init__(self,data):
        self.data = data
        self.next = []
        
    def getNext(self):
        return self.next
    
    def add(self,num):
        self.next.append(num)

        
head = Node(start)


print(head.getNext())

