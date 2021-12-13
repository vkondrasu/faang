"""
SSSP for graphs with
non-negative edge weights
"""

import math
from queue import PriorityQueue

def dijkstra(g, s):
    n = len(g)
    visited = [False] * n
    dist = [math.inf] * n

    dist[s] = 0

    pq = PriorityQueue()

    pq.insert((0,s))

    while not pq.empty():
        index, minValue = pq.get()

        visited[index] = True
        if dist[index] < minValue : continue

        for edge in g[index]:
            if visited[edge.to] : continue
            newDist = dist[index] + edge.cost

            if newDist < dist[edge.to]:
                dist[edge.to] = newDist
                pq.put((newDist, edge.to))

    return dist 