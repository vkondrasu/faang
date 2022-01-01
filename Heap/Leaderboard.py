class Leaderboard:

    def __init__(self):
        self.scores = {}
        
        

    def addScore(self, playerId: int, score: int) -> None:
        if playerId in self.scores:
            self.scores[playerId] += score
        else:
            self.scores[playerId] = score
        

    def top(self, K: int) -> int:
        heap = []
        
        for x in self.scores.values():
            heapq.heappush(heap, x)
            if len(heap) > K:
                heapq.heappop(heap)
                
        res = 0
        
        while heap:
            res += heapq.heappop(heap)
            
        return res
            
        

    def reset(self, playerId: int) -> None:
        if playerId in self.scores:
            del self.scores[playerId]