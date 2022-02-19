from collections import Counter

class Solution:
    #LC 1160. Find Words That Can Be Formed by Characters
    #Another way solving having countarray with 26 characters
    #make a copy of the countarray to check for each word
    def countCharacters(self, words: List[str], chars: str) -> int:
        resource = Counter(chars)
        
        result = 0
        for word in words:
            wordCounter = Counter(word)
            possible = True
            for key in wordCounter:
                if wordCounter[key] > resource[key]:
                    possible = False
                    break
                    
            if possible:
                result += len(word)
                
        return result
    #LC 79. Word Search
    def exist(self, board: List[List[str]], word: str) -> bool:
        '''
        start : backtracking code
        '''
        def backTrack(row, col, suffix):
            if len(suffix) == 0:
                return True
            
            if row < 0 or row == rows or col < 0 or col == cols or board[row][col] != suffix[0]:
                return False
            
            result = False
            
            board[row][col] = '#'
            
            dr = [0,0,1,-1]
            dc = [1,-1,0,0]
            
            for i in range(4):
                result = backTrack(row+dr[i], col+dc[i], suffix[1:])
                if result :
                    break
                    
            board[row][col] = suffix[0]
            
            return result
        '''
        end : backtracking code
        '''
        
        rows = len(board)
        cols = len(board[0])
        
        for row in range(rows):
            for col in range(cols):
                if backTrack(row, col, word):
                    return True
                
        return False