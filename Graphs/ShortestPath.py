from typing import Deque

"""
solve method constructs the shortest path possible 
as we mark visited first time an element is seen -- shortest path in BFS manner
"""


class ShortestPath:
    def solve(self,s, g):
        q = Deque()
        q.append(s)

        #print("added ", s, " to queue")

        n = len(g)
        visited = [False]*n

        prev=[None] * n

        while len(q) > 0:
            node = q.popleft()
            #print("deleted ", node, " from queue")

            visited[node] = True

            for next in g[node]:
                if not visited[next]:
                    q.append(next)
                    #print("added ", next, " to queue")
                    prev[next] = node

        #print(prev)
        return prev


    def getPath(self, s, e, prev):
        path = []
        at = e
        while prev[at] is not None:
            print( "checking ", at)
            path.append(prev[at])
            at = prev[at]

        path.reverse()

        print(path)

        if path[0] == s:
            return path

        return []

    
    def finsShortestPath(self, s, e, g):

        prev = self.solve(s, g)

        return self.getPath(s,e,prev)


s = ShortestPath()
path = s.finsShortestPath(0,13,[[8],[5],[9],[9],[0],[16,17],[11],[6],[4,14],[15],[],[7],[],[0],[0,13],[2,10],[],[]])
print(path)

        

