"""

LC 1244

using a sorted map




Time Complexity:

    O(logN)O(\text{log}N)O(logN) for addScore. This is because each addition to the BST takes a logarithmic time for search. The addition itself once the location of the parent is known, takes constant time.
    O(logN)O(\text{log}N)O(logN) for reset since we need to search for the score in the BST and then update/remove it. Note that this complexity is in the case when every player always maintains a unique score.
    It takes O(K)O(K)O(K) for our top function since we simply iterate over the keys of the TreeMap and stop once we're done considering K scores. Note that if the data structure doesn't provide a natural iterator, then we can simply get a list of all the key-value pairs and they will naturally be sorted due to the nature of this data structure. In that case, the complexity would be O(N)O(N)O(N) since we would be forming a new list.

Space Complexity:

    O(N)O(N)O(N) used by the scores dictionary. Also, if you obtain all the key-value pairs in a new list in the top function, then an additional O(N)O(N)O(N) would be used. 

"""

from sortedcontainers import SortedDict

class Leaderboard:

    def __init__(self):
        self.scores = {}
        self.sortedScores = SortedDict()
        
        

    def addScore(self, playerId: int, score: int) -> None:
        if playerId in self.scores:
            prevScore = self.scores[playerId]
            newScore = prevScore + score
            self.scores[playerId] = newScore
            
            val = self.sortedScores.get(-prevScore)
            if val == 1:
                del self.sortedScores[-prevScore]
            else:
                self.sortedScores[-prevScore] = val - 1 
            
            self.sortedScores[-newScore] = self.sortedScores.get(-newScore, 0) + 1  
            
        else:
            self.scores[playerId] = score
            self.sortedScores[-score] = self.sortedScores.get(-score, 0) + 1
        

    def top(self, K: int) -> int:
        count, total = 0, 0
        
        for key,value in self.sortedScores.items():
            times = self.sortedScores.get(key)
            
            for _ in range(times):
                total += -key
                count += 1
                
                if count == K:
                    break
                    
            if count == K:
                break
                
        return total
            
        

    def reset(self, playerId: int) -> None:
        prevScore = self.scores[playerId]
        
        if self.sortedScores[-prevScore] == 1:
            del self.sortedScores[-prevScore]
        else:
            self.sortedScores[-prevScore] -= 1
            
        if playerId in self.scores:
            del self.scores[playerId]
        


# Your Leaderboard object will be instantiated and called as such:
# obj = Leaderboard()
# obj.addScore(playerId,score)
# param_2 = obj.top(K)
# obj.reset(playerId)