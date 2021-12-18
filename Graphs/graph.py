from collections import defaultdict 
class Graph:

  # Constructor
  def __init__(self, vertices):
    self.graph = defaultdict(list)
    self.vertices = vertices
    
  def addEdge(self, u, v):
    self.graph[u].append(v) 