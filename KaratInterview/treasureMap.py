from collections import deque

grid = [[-1,0,0,-1,0],[0,-1,0,-1,0],[0,0,0,-1,0],[0,-1,0,0,-1],[-1,0,0,-1,0]]

rows = len(grid)
cols = len(grid[0])

def getValidMoves(cur_row, cur_col):

    dr = [0,0,-1,1]
    dc = [-1,1,0,0]

    result = []

    for i in range(4):
        new_row = cur_row + dr[i]
        new_col = cur_col + dc[i]

        if new_row > -1 and new_row < rows and new_col > -1 and new_col < cols and grid[new_row][new_col] != -1:
            result.append([new_row, new_col])

    return result


'''
print(getValidMoves(3, 2))
print(getValidMoves(3, 3))
print(getValidMoves(1, 0))
'''


def isReachable(cur_row, cur_col, end_row, end_col):
    q = deque()
    q.append((cur_row, cur_col))

    visited = []

    for i in range(rows):
        visited.append([False]*cols)

    visited[cur_row][cur_col] = True
    while q:
        row, col = q.popleft()
        for  move in getValidMoves(row, col):
            if not visited[move[0]][move[1]] :
                if move[0] == end_row and move[1] == end_col:
                    return True
                else:
                    visited[move[0]][move[1]] = True
                    q.append((move[0], move[1]))

    return False

assert(isReachable(0,1,4,4) == False)
assert(isReachable(0,1,4,1) == True)