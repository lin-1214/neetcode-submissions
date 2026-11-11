class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        rows = len(grid)
        cols = len(grid[0])
        d = deque()
        INF = 2147483647

        # pick out the treasure place
        for r in range(rows):
            for c in range(cols):
                if (grid[r][c] == 0):
                    d.append((r, c))

        
        while d:
            # implement BFS
            r, c = d.popleft()
            for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                if (r + dr) >= 0 and (r + dr) < rows and (c + dc) >= 0 and (c + dc) < cols and grid[r + dr][c + dc] == INF:
                    grid[r + dr][c + dc] = grid[r][c] + 1

                    # update new nodes to deque
                    d.append((r+dr, c+dc))
        