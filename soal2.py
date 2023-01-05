class Node:
    def __init__(self,data,priority) -> None:
        self._data = data
        self._priority = priority
        self._next = None
        self._prev = None

class PQSTugas:
    def __init__(self) -> None:
        self._data = []
        self._head = None
        self._tail = None
        self._size = 0
    
    def isEmpty(self) -> bool: #isi kode anda
        if self._size == 0:
            return True
        else:
            return False

 
    def printAll(self) -> None: #isi kode anda
        if self.isEmpty() == True:
            print("Tidak ada tugas")
        else:
            print("=== Prioritas : Tugas ===")
            bantu = self._head
            while bantu != None:
                print(bantu._priority, ':' ,bantu._data)
                bantu = bantu._next
            print()

 
    def _addHead(self, newNode) -> None:
    #isi kode anda
        if self.isEmpty():
            self._head = newNode
    def _addTail(self, newNode) -> None:
    #isi kode anda
        if self.isEmpty():
            self._tail = newNode
 
    def _addMiddle(self, newNode) -> None:
    #isi kode anda
        bantu = self._head
        while bantu._priority < newNode:
            bantu._next
            

 
    def add(self, data, priority) -> None:
        #isi kode anda
        baru = Node(data, priority)
        if self.isEmpty():
            self._head =baru
            self._tail =baru
        else:
            self._tail._next = baru
            self._tail = baru
        self._size = self._size + 1

        # baru = Node(data, priority)
        # if self.isEmpty():
        #     self._head = baru
        #     self._tail = baru
        # else:
        #     bantu = 0
        #     while data[bantu][1] < priority:
        #         bantu +=1
        #     self._data.insert(bantu, (data,priority))

        # data = [int(priority),data]
        # self._data.append(data)
        # self._data.sort()
        # self._size +=1
 
    def remove(self) -> None:
    #isi kode anda
        self._data.pop(0)
 
    def removePriority(self, priority) -> None:
    #isi kode anda
        list2 = []
        for x in range(len(self._data)):
            if self._data[x][1] == priority:
                del self._data[x][1]
        for y in range(len(self._data)):
            if len(self._data[y]) == 1:
                pass
            else:
                list2.append(self._data[y])
        
        self._data = list2
        self._size -= 1



if __name__ == "__main__":
 tugasKu = PQSTugas()
 tugasKu.add("StrukDat",1)
 tugasKu.add("Menyapu", 5)
 tugasKu.add("Cuci Baju", 4)
 tugasKu.add("Beli Alat Tulis", 3)
 tugasKu.add("Cuci Sepatu", 4)
 tugasKu.printAll()
#  tugasKu.remove()
#  tugasKu.printAll()
#  tugasKu.removePriority(2)
 tugasKu.removePriority(4)
 tugasKu.printAll()