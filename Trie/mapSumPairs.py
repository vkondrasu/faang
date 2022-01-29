'''
LC 677. Map Sum Pairs
'''

class TrieNode:
    def __init__(self):
        self.children = {}
        self.value = 0

class MapSum:

    def __init__(self):
        self.root = TrieNode()
        

    def insert(self, key: str, val: int) -> None:
        cur = self.root 
        for c in key:
            if c not in cur.children:
                cur.children[c] = TrieNode()
            cur = cur.children[c]
        cur.value = val
        
    def getSum(self, node: TreeNode) -> None:
        if not node:
            return
        summ = node.value
        for child in node.children:
            summ += self.getSum(node.children[child])
            
        return summ
            
        

    def sum(self, prefix: str) -> int:
        cur = self.root
        for c in prefix:
            if c not in cur.children:
                return 0
            cur = cur.children[c]
        result = self.getSum(cur) 
        
        return result
        


# Your MapSum object will be instantiated and called as such:
# obj = MapSum()
# obj.insert(key,val)
# param_2 = obj.sum(prefix)