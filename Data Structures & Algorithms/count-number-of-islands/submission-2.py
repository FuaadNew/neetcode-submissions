from typing import List

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows, cols = len(grid), len(grid[0])
        visit = set()

        def dfs(r, c):
            # If out of bounds or the cell is water ("0") or already visited
            if r < 0 or c < 0 or r == rows or c == cols or grid[r][c] == "0" or (r, c) in visit:
                return
            visit.add((r, c))  # Mark the cell as visited

            # Explore all 4 directions
            dfs(r + 1, c)  # Down
            dfs(r - 1, c)  # Up
            dfs(r, c + 1)  # Right
            dfs(r, c - 1)  # Left

        island_count = 0  # Variable to count the number of islands

        for r in range(rows):
            for c in range(cols):
                # If the cell is land ("1") and hasn't been visited, start DFS
                if grid[r][c] == "1" and (r, c) not in visit:
                    dfs(r, c)  # Explore the entire island
                    island_count += 1  # Increment the island count

        return island_count
