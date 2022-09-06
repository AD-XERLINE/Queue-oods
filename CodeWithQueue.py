class Queue: 

    def __init__(self, list = None): 
        if list == None: 
            self.items = []
        else:
            self.items = list

    def enQueue(self, i): 
        self.items.append(i)

    def deQueue(self): 
        return self.items.pop(0)

    def isEmpty(self): 
        return self.items == []

    def size(self): 
        return len(self.items)
        
lst = input("Enter code,hint : ").split(',')
q = Queue()
q.enQueue(list(lst[0]))
q.enQueue(list(lst[1]))
# [[ในนี้คคือเลือกอาเรย์ที่เท่าไหร่][ในนี้คือเลือกตัวในอาเรย์นั้น]]
a = ord(q.items[0][0]) #ต้องทำใว้นอกรูป
b = ord(q.items[1][0]) #ต้องทำใว้นอกรูป
c = b-a

p = []
for i in range(len(q.items[0])):
    p += chr((ord(q.items[0][i])+c))
    print(p)
