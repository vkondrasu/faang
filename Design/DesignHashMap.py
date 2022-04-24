'''
LC 706. Design HashMap
'''
class MyHashMap:

    def __init__(self):
        self.buckets = [[[] for i in range(10)] for j in range(100)]
        

    def put(self, key: int, value: int) -> None:
        bucket_index = key % 100
        row_index = key % 10
        n = len(self.buckets[bucket_index][row_index])
        for i in range(n):
            if self.buckets[bucket_index][row_index][i][0] == key:
                self.buckets[bucket_index][row_index][i][1] = value
                return
        self.buckets[bucket_index][row_index].append([key,value])
        

    def get(self, key: int) -> int:
        bucket_index = key % 100
        row_index = key % 10
        n = len(self.buckets[bucket_index][row_index])
        for i in range(n):
            if self.buckets[bucket_index][row_index][i][0] == key:
                return self.buckets[bucket_index][row_index][i][1]
        return -1

    def remove(self, key: int) -> None:
        bucket_index = key % 100
        row_index = key % 10
        n = len(self.buckets[bucket_index][row_index])
        for i in range(n):
            if self.buckets[bucket_index][row_index][i][0] == key:
                del self.buckets[bucket_index][row_index][i]
                return


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)