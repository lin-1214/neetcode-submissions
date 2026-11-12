class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        rows, cols = len(heights), len(heights[0])

        # remember where each ocean can flow to
        pac, atl = set(), set()

        # do dfs from both pac and atl
        def dfs(r, c, ocean):
            ocean.add((r, c))

            for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                nr, nc = r + dr, c + dc
                if nr >= 0 and nr < rows and nc >= 0 and nc < cols and heights[r][c] <= heights[nr][nc] and (nr, nc) not in ocean:
                    dfs(nr, nc, ocean)

        for r in range(rows):
            dfs(r, 0, pac)
            dfs(r, cols - 1, atl)
        for c in range(cols):
            dfs(0, c, pac)
            dfs(rows - 1, c, atl)

        return [[r, c] for r, c in atl & pac]
