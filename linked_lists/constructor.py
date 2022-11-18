class Node:
    def __init__(self,value):
        self.value = value
        self.next = None
 
        
class LinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1
    
    def append(self,value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
            self.length += 1
            return True
    def prepend(self, value):
        new_node = Node(value)
        if self.head == None:
            self.head = new_node
            self.tail = new_node
            self.length = new_node 
        else:
            new_node.next = self.head
            self.head = new_node
            self.length += 1
            return True
  

    def pop(self):
        if self.head == None:
            return None
        elif self.length == 1:
            result = self.head
            self.head = None
            self.tail = None
            self.length = 0
            return result
        else:
            current = self.head
            while current.next.next:
                current = current.next.next
            print(self.tail)
            self.length -= 1
            current.next = None
            result = self.tail
            self.tail = current.next
            return result

    def pop_first(self):
        if self.head == None:
            return None
        elif self.length == 1:
            result = self.head
            self.head = None
            self.tail = None
            self.length -= 1
            return result
        else:
            result = self.head
            self.head = self.head.next 
            self.length -= 1
            return result

    def get(self, index):
        if index < 0 or index >= self.length:
            return None
        temp = self.head 
        for _ in range(index):
            temp = temp.next
        return temp
    
    def set_value(self, index, value):
        temp = self.get(index)
        if temp:
            temp.value = value
            return True
        return False

    def insert(self, index, value):
        if index < 0 or index > self.length:
            return None
        elif index == 0:
            return self.prepend(value)
        elif index == self.length:
            return self.append(value)   
        else:
            new_node = Node(value)
            node_at_idx = self.get(index-1)
      
            if node_at_idx and node_at_idx.next:
                new_node.next = node_at_idx.next 
                node_at_idx.next = new_node
                self.length += 1
                return True
            else:
                return None
    
    def remove(self,index):
        if index < 0 or index > self.length:
            return None
        elif index == 0:
            return self.pop_first()
        elif self.length == index:
            return self.pop()
        else:
            temp = self.get(index-1)
            if temp:
                result = temp.next
                temp.next = temp.next.next
                self.length -= 1
                return result
            else:
                return None
    
    def reverse(self):
        if self.head == None:
            return None
        elif self.length == 1:
            return True
        else:
            temp = self.head
            self.head = self.tail
            self.tail = temp
            after = temp.next
            before = None
            for _ in range(self.length):
                after = temp.next
                temp.next = before
                before = temp
                temp = after


    def print_list(self):
        temp = self.head
        while temp:
            print(temp.value)
            temp = temp.next
     
