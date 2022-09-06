
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
        #return len(self.items) == 0

    def size(self): 
        return len(self.items)

lst = input("Enter Input : ").split(',')
s = Queue()
t = Queue()
# "".join(lst)
for i in range(len(lst)):
                if lst[i][0] == "E":
                    s.enQueue((lst[i][2:]))
                    print(', '.join(s.items))
                    
                elif lst[i][0] == "D":
                    if s.items != []:
                        o = s.deQueue()
                        t.enQueue(o)
                        print(str(o) + " <- " ,end="")

                        if s.isEmpty() :
                                print("Empty")
                        else:
                            for j in range(len(s.items)):

                                if j != len(s.items)-1:
                                    print(s.items[j],end=", ")
                                
                                else:
                                    print(s.items[j])
                                    
                    else:
                        print("Empty")

if s.items == [] :
    s.enQueue("Empty")
    
if t.items == []:
    t.enQueue("Empty")

print(', '.join(t.items), ':', ', '.join(s.items))
