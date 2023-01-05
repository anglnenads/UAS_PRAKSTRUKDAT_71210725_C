class NodePelanggan:
    def __init__(self, namaPelanggan):
        self._namaPelanggan = namaPelanggan

    def getNamaPelanggan(self):
        return self._namaPelanggan

    def setnamaPelanggan(self, namaPelangganBaru):
        self._namaPelanggan = namaPelangganBaru

class WarungMakan:
    DEFAULT_CAPACITY = 5
    def __init__(self):
        self._data = [None] * WarungMakan.DEFAULT_CAPACITY
        self._size = 0
        self._front = 0

    def __len__(self):
        return self._size

    def is_empty(self):
        return self._size == 0

    def dequeue(self):

        # data = self._data[0]
        # self._data.remove(data)
        # return data
        if self.is_empty():
            print("Empty")
        
        answer = self._data[self._front]
        self._data[self._front] = None
        self._front = (self._front +1) % len(self._data)
        self._size -= 1
        # print("\n### Pelanggan", NodePelanggan.getNamaPelanggan(answer),"Selesai Membayar ###")

        listBaru = [None] * len(self._data)
        counterListBaru = 0
        for i in range (len(self._data)):
            if self._data[i] != None:
                listBaru[counterListBaru] = self._data[i]
                counterListBaru += 1
            self._data = listBaru
            self._front = 0

    def enqueue(self, namaPelanggan):
        new = NodePelanggan(namaPelanggan)
        # if self._size >= len(self._data):
        if self.__len__() >= self.DEFAULT_CAPACITY:
            self.resizeBy3(3 + self.DEFAULT_CAPACITY)
        avail = (self._front + self._size) % len(self._data)
        self._data[avail] = new
        self._size += 1
        print()



    def resizeBy3(self, cap):
        # self.DEFAULT_CAPACITY = self.DEFAULT_CAPACITY*3
        # print("### Melakukan Resize 3 ###")
        # print()

        old = self._data
        self._data = [None] * cap
        walk = self._front
        for k in range(self._size):
            self._data[k] = old[walk]
            walk = (1 + walk) % len(old)
            self._front = 0
    def printAll(self):
        print("\n=== WarungMakan ===")
        for i in range(len(self._data)):
            if self._data[i] != None:
                print(i+1,end=". ")
                print(self._data[i].getNamaPelanggan())
            else:
                print(i+1,end=". ")
                print("Kosong")

wm = WarungMakan()
wm.enqueue("Pelanggan A")
wm.enqueue("Pelanggan B")
wm.enqueue("Pelanggan C")
wm.enqueue("Pelanggan D")
wm.enqueue("Pelanggan E")
wm.printAll()

wm.enqueue("Pelanggan F")
wm.enqueue("Pelanggan G")
wm.printAll()

wm.dequeue()
wm.dequeue()
wm.dequeue()
wm.printAll()