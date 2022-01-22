
class ListNode:
    def __init__(self, key, value):
        self.val = value
        #print("adding key", key)
        self.key = key
        self.next = None
        self.prev = None

class LRUCache:

    def __init__(self, capacity: int):
        self.hashMap = {}
        self.capacity = capacity
        self.head = None
        self.tail = None
        
    def removeTail(self):
        tail = self.adjustTail()
        del self.hashMap[tail]
    
    def adjustTail(self):
        temp = self.tail
        self.tail = temp.prev
        self.tail.next = None
        return temp.key
        
    def insertAtHead(self, node):
        if self.head == None:
            self.head = self.tail = node
        else:
            self.head.prev = node
            node.next = self.head
            node.prev = None
            self.head = node
    
    def adjustPointers(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev
        
        

    def get(self, key: int) -> int:
        if key in self.hashMap:
            #is at head
            if self.head == self.hashMap[key]:
                return self.hashMap[key].val
            elif self.tail == self.hashMap[key]:
                node = self.hashMap[key]
                self.adjustTail()
                self.insertAtHead(node)
                return node.val
            else:
                node = self.hashMap[key]
                self.adjustPointers(node)
                self.insertAtHead(node)
                return node.val
        else:
            return -1
        

    def put(self, key: int, value: int) -> None:
        if key in self.hashMap:
            self.hashMap[key].val = value
            self.get(key)
        else:
            #put into hashMap
            node = ListNode(key, value)
            self.hashMap[key] = node
            
            self.insertAtHead(node)
            
            if len(self.hashMap) > self.capacity:
                self.removeTail()
        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)