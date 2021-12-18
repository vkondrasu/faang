"""
copied from educative
https://www.educative.io/module/lesson/recursion-in-python/7XMA92A4j88 
"""
from collections import defaultdict 
class Graph:

  # Constructor
  def __init__(self, vertices):
    self.graph = defaultdict(list)
    self.vertices = vertices
    
  def addEdge(self, u, v):
    self.graph[u].append(v) 