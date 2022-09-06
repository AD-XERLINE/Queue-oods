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
        
lst = input("Enter Input : ").split(',')
q1 = Queue()
q2 = Queue()
sumo = Queue()

for i in range(len(lst)):
    if lst[i][:2] == "EN":
        q1.enQueue((lst[i][3:]))
                    
    elif lst[i][:2] == "ES":
        q2.enQueue((lst[i][3:]))

    elif lst[i][:2] == "D":

        # print(sumo.items)
        if q1.items == [] and q2.items == []:
            print("Empty")                 
        elif q2.items != []:
            print(q2.deQueue())
        else:
            print(q1.deQueue())

    

# ใช้ 2 คิว ตัวนึง ES ตัวนึง EN ทุกครั้้งที่เข้าเสรจให้เอามารวมกันแล้วค่อย pop ออก จากนั้นพอเริ่มใหม่ให้ลบ คิวที่รวม ES EN
