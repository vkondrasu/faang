'''
LC 705. Design HashSet
'''
class MyHashSet:

    def __init__(self):
        self.keyrange = 769
        self.bucketArray = [Bucket() for i in range(self.keyrange)]
    
    def _hash(self, key):
        return key % self.keyrange

    def add(self, key: int) -> None:
        bucket_index = self._hash(key)
        self.bucketArray[bucket_index].insert(key)
        

    def remove(self, key: int) -> None:
        bucket_index = self._hash(key)
        self.bucketArray[bucket_index].delete(key)
        

    def contains(self, key: int) -> bool:
        bucket_index = self._hash(key)
        return self.bucketArray[bucket_index].exists(key)
    
class Bucket:
    def __init__(self):
        self.tree = BSTree()
        
    def insert(self, val):
        self.tree.root = self.tree.insert(self.tree.root, val)
    
    def delete(self, val):
        self.tree.root = self.tree.delete(self.tree.root, val)
        
    def exists(self, val):
        return self.tree.search(self.tree.root, val) != None

class TreeNode:
    def __init__(self, value):
        self.val = value
        self.left = None
        self.right = None
        
class BSTree:
    def __init__(self):
        self.root = None
        
    def search(self,root, val):
        if root is None or root.val == val:
            return root
        if val < root.val:
            return self.search(root.left, val)
        else:
            return self.search(root.right, val)
        
    def insert(self, root, val):
        if not root:
            return TreeNode(val)
        if val > root.val:
            root.right = self.insert(root.right, val)
        elif val == root.val:
            return root
        else:
            root.left = self.insert(root.left, val)
        return root
    
    def predecessor(self, root):
        root = root.left
        while root.right:
            root = root.right
        return root.val
    
    def successor(self, root):
        root = root.right
        while root.left:
            root = root.left
        return root.val
    
    def delete(self, root, val):
        if not root:
            return None
        if val > root.val:
            root.right = self.delete(root.right, val)
        elif val < root.val:
            root.left = self.delete(root.left, val)
        else:
            if not (root.left or root.right):
                root = None
            elif root.right:
                root.val = self.successor(root)
                root.right = self.delete(root.right, root.val)
            else:
                root.val = self.predecessor(root)
                root.left = self.delete(root.left, root.val)
        return root
    
# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)