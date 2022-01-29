'''
LC 648. Replace Words
'''

class TrieNode:
    def __init__(self):
        self.children = {}
        self.endOfWord = False
class Trie:

    def __init__(self):
        self.root = TrieNode()
        

    def insert(self, word: str) -> None:
        cur = self.root
        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode()
            cur = cur.children[c]
            
        cur.endOfWord = True
        

    def getPrefix(self, word: str) -> bool:
        cur = self.root
        sofar = ""
        for c in word:
            if cur.endOfWord:
                return sofar
            sofar += ""+c
            if c not in cur.children:
                return False
            
                
            cur = cur.children[c]
            
        return sofar

class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        t = Trie()
        for word in dictionary:
            t.insert(word)
            
        words = sentence.split(" ")
        for i in range(len(words)):
            prefix = t.getPrefix(words[i])
            if prefix:
                words[i] = prefix
                
        return " ".join(words)
        