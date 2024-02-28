class Node:
    def __init__(self,value):
        self.value = value
        self.next=None

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def append(self,value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
            
        else:
            self.tail.next = new_node
            self.tail = new_node

        self.length += 1

    def prepend(self,value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node

        else:
            new_node.next = self.head
            self.head = new_node

        self.length += 1

    def insert(self,index,value):
        new_node  = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        elif index == 0:
            new_node.next = self.head
            self.head = new_node
        
        else:
            temp_node = self.head
            for _ in range(index-1):
                temp_node = temp_node.next
            
            new_node.next = temp_node.next
            temp_node.next = new_node
        self.length += 1

    def traverse(self):
        current_node = self.head
        while current_node is not None:
            print(current_node.value)
            current_node = current_node.next


    
    def __str__(self):
        temp_node = self.head
        result = ""

        while temp_node is not None:
            result += str(temp_node.value)
            if temp_node.next is not None:
                result += "->"

            temp_node = temp_node.next

        return result
    

if __name__ == '__main__':
    linked_list = LinkedList()
    linked_list.append(1)
    linked_list.append(12)
    linked_list.append(15)
    linked_list.append(11)
    print(linked_list)
    linked_list.prepend(2)
    print(linked_list)
    linked_list.insert(0,435)
    print(linked_list)
    linked_list.traverse()

