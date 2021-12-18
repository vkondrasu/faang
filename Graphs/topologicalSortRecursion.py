"""
copied from educative
https://www.educative.io/module/lesson/recursion-in-python/7XMA92A4j88 
"""
import graph as g

def helperFunction(myGraph, currentNode, visited, result) :
  visited[currentNode] = True # Mark the current node as visited
  
  # Recur for all the adjacent vertices of currentNode
  for i in myGraph.graph[currentNode] :
    if visited[i] == False :
      helperFunction(myGraph, i, visited, result)
  
  result.insert(0, currentNode) # Push current vertex to result
  
  
def topologicalSort(myGraph) :
  visited = [False] * myGraph.vertices  # Mark all the vertices as not visited
  result = [] # Our stack to store the result/output

  for currentNode in range(myGraph.vertices) :
    if visited[currentNode] == False :
      helperFunction(myGraph, currentNode, visited, result)

  return(result)


# Driver code 
# Create a graph given in the above diagram 
myGraph = g.Graph(6) 
myGraph.addEdge(5, 2) 
myGraph.addEdge(5, 0) 
myGraph.addEdge(4, 0) 
myGraph.addEdge(4, 1) 
myGraph.addEdge(2, 3) 
myGraph.addEdge(3, 1) 

print("Topological Sort")
print(topologicalSort(myGraph))