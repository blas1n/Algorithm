class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        answer, c, r = 0, len(grid), len(grid[0])
        queue = deque([(y, x) for y in range(len(grid)) for x in range(len(grid[y])) if grid[y][x] == 2])
        while queue:
            size = len(queue)
            for _ in range(size):
                y, x = queue.popleft()
                for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                    nx, ny = x + dx, y + dy
                    if nx < 0 or nx >= r or ny < 0 or ny >= c:
                        continue
                    if grid[ny][nx] == 1:
                        grid[ny][nx] = 2
                        queue.append([ny, nx])
            if queue:
                answer += 1
        return -1 if any(1 in row for row in grid) else answer