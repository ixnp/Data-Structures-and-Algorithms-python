class Node:
    def __init__(self,value):
        self.value = value
        self.next = None
        self.prev = None
 
        
class DoublyLinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

    def append(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
            self.length += 1
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node
            self.length += 1
            return True

    def pop(self):
        if self.length == 0:
            return None
        elif self.length == 1:
            temp = self.head
            self.head = None
            self.tail = None
            self.length = 0
            return temp
        else:
            temp = self.tail
            self.tail = self.tail.prev
            self.tail.next = None
            self.length -= 1
            return temp
    
    def prepend(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
            self.length += 1
        else:
            new_node.next = self.head
            self.head.prev = new_node 
            self.head = new_node
            self.length += 1
    
    def pop_first(self):
        if self.length == 0:
            return None
        elif self.length == 1:
            temp = self.head
            self.head = None
            self.tail = None
            self.length -=1
            return temp
        else:
            temp = self.head
            self.head.next.prev = None
            self.head = self.head.next
            self.length -=1
            return temp
        
    def get(self, index):
        if index < 0 or index >= self.length:
            return None
        elif index < self.length/2:
            temp = self.head
            for _ in range(index):
                temp = temp.next 
            return temp
        else:
            temp = self.tail
            for _ in range(self.length, index, -1):
                temp = temp.prev
            return temp
    def set_value(self, index, value):
        temp = self.get(index)
        if temp:
            temp.value = value
            return True
        else:
            return False

    def insert(self, index, value):
        if index < 0 or index > self.length:
            return False
        if index == 0:
            return self.prepend(value)
        if index == self.length:
            return self.append(value)

        new_node = Node(value)
        before = self.get(index - 1)
        after = before.next

        new_node.prev = before
        new_node.next = after
        before.next = new_node
        after.prev = new_node
        
        self.length += 1   
        return True  

    def remove(self, index):
        if index < 0 or index >= self.length:
            return None
        elif index == 0:
            return self.pop_first()
        elif index == self.length - 1:
            return self.pop()
        else:
            temp = self.get(index)
            
            temp.next.prev = temp.prev
            temp.prev.next = temp.next
            temp.next = None
            temp.prev = None

            self.length -= 1
            return temp
  
    def print_list(self):
        temp = self.head
        while temp:
            print(temp.value)
            temp = temp.next


