from collections import deque
class Solution:
    def bfs(self, i, j, grid, visit):
        q = deque([(i, j)])
        visit.add((i, j))  # Mark the current cell as visited
        possible_neighbors = [
            [0, -1], [-1, 0], [0, 1], [1, 0]
        ]
        while q:
            coord_i, coord_j = q.popleft()
            for n in possible_neighbors:
                new_i, new_j = coord_i + n[0], coord_j + n[1]
                # Check if the new coordinates are within the grid boundaries
                if (0 <= new_i < len(grid)) and (0 <= new_j < len(grid[0])):
                    if grid[new_i][new_j] == "1" and (new_i, new_j) not in visit:
                        q.append((new_i, new_j))
                        visit.add((new_i, new_j))
        return visit

    def numIslands(self, grid: List[List[str]]) -> int:
        rows, cols = len(grid), len(grid[0])
        visited = set()
        islands = 0        
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == "1" and not (i,j) in visited:
                    visited = visited.union(self.bfs(i,j,grid, visited))
                    islands += 1
        return islands


                        
