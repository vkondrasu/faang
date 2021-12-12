from typing import Deque


class DungeonGrid:
    def __init__(self, g) -> None:
        self.g = g
        self.r = len(g)
        self.c = len(g[0])
        #print (self.r, self.c)
        #print(g)


    def exploreNeighbours(self, cell):
        dr = [-1,0,+1,0]
        dc = [0,-1,0,+1]

        for i in range(4):
            rr = cell[0] + dr[i]
            cc = cell[1] + dc[i]

            #print("current cell ", (rr,cc))

            if rr < 0 or rr >= self.r : 
                #print("row ", rr, " out of bounds")
                continue
            if cc < 0 or cc >= self.c : 
                #print("column ", cc, " out of bounds")
                continue
            if self.visited[rr][cc] : 
                #print ( rr, cc, " already visited")
                continue
            self.visited[rr][cc] = True
            if self.g[rr][cc] == "#" : 
                #print ( rr, cc, " is #")
                continue

            
            #print("Added to queue ", (rr,cc))
            self.q.append((rr,cc))

            self.next_layer_count += 1

    def getMovesToGetOut(self):
        
        self.visited = []
        temp = []
        
        for i in range(self.r):
            for j in range(self.c):
                temp.append(False)
            self.visited.append(temp)
            temp = []

        #print(self.visited)

        move_count = 0
        foundEnd = False

        self.q = Deque()
        self.q.append((0,0))
        self.visited[0][0] = True

        #print(self.visited)

        self.current_layer_count = 1
        self.next_layer_count = 0

        while len(self.q) > 0:
            cell = self.q.popleft()
            #print("Exploring ", cell)
            """

            if self.visited[cell[0]][cell[1]]:
                continue
            
            """
            
            if self.g[cell[0]][cell[1]] == "E":
                foundEnd = True
                break

            
            
            if self.g[cell[0]][cell[1]] != "#":
                self.exploreNeighbours(cell)

            self.current_layer_count -= 1

            if self.current_layer_count == 0:
                self.current_layer_count = self.next_layer_count
                self.next_layer_count = 0
                move_count += 1

        if foundEnd :
            return move_count
        return -1


s = DungeonGrid([ ["S",".",".","#","."], [".",".",".",".","."], [".",".",".",".","."], [".","E",".",".","#"], [".",".","#","#","."] ])
print(s.getMovesToGetOut())

"""
[
    ["S",".".".","#","."],
    [".",".".".",".","."],
    [".",".".".",".","."],
    [".",".".".",".","#"],
    [".","."."#","E","."]
]

"""


