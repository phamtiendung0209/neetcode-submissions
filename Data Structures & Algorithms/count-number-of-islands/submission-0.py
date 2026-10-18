class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows, cols = len(grid), len(grid[0])
        discovered = set()
        islands = 0

        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "0" or (r, c) in discovered:
                    continue

                islands += 1
                stack = [(r, c)]
                discovered.add((r, c))

                while stack:
                    row, col = stack.pop()

                    for dr, dc in directions:
                        nr, nc = row + dr, col + dc

                        if (0 <= nr < rows and
                            0 <= nc < cols and
                            grid[nr][nc] == "1" and
                            (nr, nc) not in discovered):

                            discovered.add((nr, nc))
                            stack.append((nr, nc))

        return islands