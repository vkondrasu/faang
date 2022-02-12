'''
LC 127. Word Ladder
'''
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        
        if beginWord == endWord:
            return 0
        
        def isOnedistance(word1, word2):
            count = 0
            for i in range(len(word1)):
                if word1[i] != word2[i]:
                    if count > 0:
                        return False
                    count += 1
                    
            return True
        
        word_set = set(wordList)
        
        q = deque()
        q.append((beginWord, 1))
        temp_word_set = set(word_set)
        
        while q:
            cur_word, cur_count = q.popleft()
            for word in word_set:
                if isOnedistance(word, cur_word): 
                    if word == endWord:
                        return cur_count+1
                    q.append((word, cur_count+1))
                    temp_word_set.remove(word)
                    
            word_set = set(temp_word_set)
            
        return 0