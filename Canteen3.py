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

def search(N) :
    for i in range(len(temp.items)):
        for j in range(len(lst[0])):
            if lst[0][j][0] == temp.items[i] and N in lst[0][j]:
                return i
           
                

lst = list(map(str, input("Enter Input : ").split('/')))

lst[0] = list(lst[0].split(','))
lst[1] = list(lst[1].split(','))
temp = Queue()
sum = Queue()
ram = Queue()

for i in range(len(lst[0])):
    lst[0][i] = list(lst[0][i].split(" "))
    # print(lst[0])
for i in range(len(lst[0])):
    if not lst[0][i][0] in temp.items:
        temp.enQueue(lst[0][i][0])
# print(temp.items)
# print(search(str(107)))


for i in range(len(lst[1])):
    if lst[1][i][:1] == "E":
        
        # print(lst[1][i][2:])
        if sum.items == []:
            sum.enQueue(lst[1][i][2:])   
        #     sum.enQueue(lst[1][i][2:])
        else:
            t = 1
            ram.items.clear()
            # print((sum.items))
            for k in range(len(sum.items)):
                ram.enQueue(search(sum.items[k]))
            # print(ram.items)
            for j in range(len(sum.items)):
                
                if search(lst[1][i][2:]) == search(sum.items[-t]):
                    # print("+",t,search(lst[1][i][2:]),lst[1][i][2:],search(sum.items[-t]),sum.items[-t])
                    if t == 1:
                        sum.enQueue(lst[1][i][2:])
                        break
                    else:
                        sum.items.insert(1-t,lst[1][i][2:])
                        # print(sum.items)
                        break   
                # elif search(lst[1][i][2:]) < search(sum.items[-t]):
                    
                #     sum.items.insert(-t,lst[1][i][2:])
                #     break

                elif not search(lst[1][i][2:]) in ram.items:
                    # print(lst[1][i][2:])
                    sum.enQueue(lst[1][i][2:])
                    break

                else:
                    print('',end='')
                t += 1
            # print("--------------")   
        
        # print(sum.items)
    elif lst[1][i][:1] == "D":
        # print(lst[1][i][:1])
        if sum.items != [] :
            print(sum.deQueue())
        else:
            print("Empty")


# ไล่จากตัวหลังดูว่าหน้ามันเป็นกลุ่มเดียวกันไหมถ้าใช้ก็ลงตรงหลังมันเลย
# เรียงลำดับผิด