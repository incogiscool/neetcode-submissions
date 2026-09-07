class LinkedList:
    
    def __init__(self):
        self.list = [];
        self.length = 0;

    
    def get(self, index: int) -> int:
        if index < self.length and index >= 0:
            return self.list[index]
        else:
            return -1

        

    def insertHead(self, val: int) -> None:
        self.list = [val, *self.list]
        self.length += 1

    def insertTail(self, val: int) -> None:
        self.list = [*self.list, val]
        self.length += 1

    def remove(self, index: int) -> bool:
        if index < self.length and index >= 0:
            new_arr = []

            for i in range(self.length):
                if i == index:
                    continue
                new_arr.append(self.list[i])

            self.length -= 1

            self.list = new_arr

            return True
        else:
            return False


        

    def getValues(self) -> List[int]:
        return self.list
        
